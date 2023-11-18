from Course import Course
from Admin import Admin
from Applicant import Applicant
from CourseSection import CourseSection
from Faculty import Faculty
from FacultySection import FacultySection
from Staff import Staff
from Student import Student
from StudentSection import StudentSection
from Section import Section
from User import User

from peewee import Model, SqliteDatabase, AutoField, ForeignKeyField, CharField, IntegerField

db = SqliteDatabase('studentdatabase.db')

class User(Model):
    userID = AutoField(primary_key=True)
    fname = CharField()
    mname = CharField(null=True)
    lname = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()

class Student(User):
    studentID = AutoField(primary_key=True)
    uploadeddocs = CharField()
    grades = IntegerField()
    enrolledSections = CharField()

class Staff(User):
    staffID = AutoField(primary_key=True)

class Admin(User):
    adminID = AutoField(primary_key=True)

class Faculty(User):
    facultyID = AutoField(primary_key=True)
    assignedSections = CharField()

class Applicant(User):
    applicantID = AutoField(primary_key=True)
    uploadeddocs = CharField()

class Course(Model):
    courseID = AutoField(primary_key=True)
    coursename = CharField()

class Section(Model):
    sectionID = AutoField(primary_key=True)
    sectionname = CharField()
    course = ForeignKeyField(Course, backref='sections')

class CourseSection(Model):
    courseID = ForeignKeyField(Course, backref='course_sections')
    sectionID = ForeignKeyField(Section, backref='course_sections')

class FacultySection(Model):
    facultyID = ForeignKeyField(Faculty, backref='faculty_sections')
    sectionID = ForeignKeyField(Section, backref='faculty_sections')

class StudentSection(Model):
    studentID = ForeignKeyField(Student, backref='student_sections')
    sectionID = ForeignKeyField(Section, backref='student_sections')

# Set the database for all models
for model in [User, Student, Staff, Admin, Faculty, 
              Applicant, Course, Section, CourseSection, 
              FacultySection, StudentSection]:
    model._meta.database = db

# Connect to the database and create tables
db.connect()
db.create_tables([User, Student, Staff, Admin, Faculty,
                  Applicant, Course, Section, CourseSection,
                  FacultySection, StudentSection], safe=True)

class Database:
    def __init__(self, database_path='studentdatabase.db'): # Initialize the database.
        self.db = SqliteDatabase(database_path)
        self.connect()

    def __enter__(self): # Enter the context.
        self.db.__enter__()

    def __exit__(self, exc_type, exc_value, traceback): # Close the database connection when exiting the context.
        self.db.__exit__(exc_type, exc_value, traceback)

    def connect(self):
        # Connect to the database.
        with self:
            self.db.connect()

    def create_tables(self):
        # Create tables in the database for all defined models.
        with self:
            self.db.create_tables([User, Student, Staff, 
                                   Admin, Faculty, Applicant, 
                                   Course, Section, CourseSection, 
                                   FacultySection, StudentSection], safe=True)

    def save_database(self, path='../data/'): # Save the database and close the connection.
        with self:
            self.db.close()

    def get_all(self, model): # Get all records for a given model.
        return model.select()

    def get_all_by_condition(self, model, condition): # Get all records for a given model based on a condition.
        return model.select().where(condition)

    def create_user(self, model, **kwargs):
        with self.db.atomic():
            try:
                return model.create(**kwargs)
            except IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    print(f"Error: A user with this email already exists for {model.__name__}.")
                else:
                    print(f"Error: IntegrityError - {e}")
                return None

    def create_student(self, **kwargs): # Create a new student in the database.
        return self.create_user(Student, **kwargs)

    def create_staff(self, **kwargs): # Create a new staff member in the database.
        return self.create_user(Staff, **kwargs)

    def create_admin(self, **kwargs): # Create a new admin in the database.
        return self.create_user(Admin, **kwargs)

    def create_faculty(self, **kwargs): # Create a new faculty member in the database.
        return self.create_user(Faculty, **kwargs)

    def create_applicant(self, **kwargs): # Create a new applicant in the database.
        return self.create_user(Applicant, **kwargs)

    def create_course(self, **kwargs): # Create a new course in the database.
        with self.db.atomic():
            try:
                return Course.create(**kwargs)
            except IntegrityError:
                print(f"Error: A course with this name already exists.")
                return None

    def create_section(self, **kwargs):# Create a new section in the database.
        with self.db.atomic():
            try:
                return Section.create(**kwargs)
            except IntegrityError:
                print(f"Error: A section with this name already exists.")
                return None

    def create_course_section(self, **kwargs):# Create a new course-section relationship in the database.
        with self.db.atomic():
            return CourseSection.create(**kwargs)

    def create_faculty_section(self, **kwargs): # Create a new faculty-section relationship in the database.
        with self.db.atomic():
            return FacultySection.create(**kwargs)

    def create_student_section(self, **kwargs): # Create a new student-section relationship in the database.
        with self.db.atomic():
            return StudentSection.create(**kwargs)

if __name__ == "__main__":
    with Database() as db:
        # Create a student
        db.create_student(
            fname='John',
            mname='N/A',
            lname='Doe',
            email='john@elmwood.uni',
            password='password123',
            role='student',
            uploadeddocs='docs_path',
            grades=90,
            enrolled_sections='section_A'
        )

        # Create an admin
        db.create_admin(
            fname='Admin',
            lname='Admin',
            email='admin@admin.elmwood.uni',
            password='admin123',
            role='admin'
        )

    # Save the database (close the connection)
    db.save_database()
