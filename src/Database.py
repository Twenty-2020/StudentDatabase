from typing import List
from peewee import *
from datetime import datetime
import shutil
import os

from User import User
from Admin import Admin
from Applicant import Applicant
from Student import Student
from Faculty import Faculty
from Staff import Staff
from Course import Course
from Section import Section
from UserDocuments import UserDocuments
from StudentGrades import StudentGrades
from CourseSection import CourseSection
from StudentSection import StudentSection
from FacultySection import FacultySection

# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)

class Database:
    def __init__(self,db):
        self.db = db
        self.db.connect()
        self.db.create_tables([User, Student, Staff, Admin, Faculty, Applicant, Course, Section, CourseSection, FacultySection, StudentSection, UserDocuments, StudentGrades, UserDocuments], safe = True)


    #Create Users Functions

    def createApplicant(self, fname: str, mname: str, lname: str, email: str, role: str = 'Applicant') -> Applicant:
        applicantId = self.getLastID(role) + 1
        #checks if the email already exists
        if User.select().where(User.email == email).exists():
            raise ValueError(f"A user with the email {email} already exists.")
        #creates a user with the given data
        user = User.create(fname = fname, mname = mname, lname = lname, email = email, password=None, role=role)
        return Applicant.create(userID = user.userID, applicantID = applicantId, email = email, fname = fname, mname = mname, lname = lname, password = None, role = role)
    
    def createStudent(self, fname: str, mname:str, lname: str, studentID: int = 0, role: str = 'Student') -> Student:
        studentId = self.getLastID(role) + 1
        password = lname + str(studentId)
        email = str(studentId) + "@elmwood.edu.ph"
        #checks if the email already exists
        if User.select().where(User.email == email).exists():
            raise ValueError(f"A user with the email {email} already exists.")
        #creates a user with the given data
        user = User.create(fname = fname, mname = mname, lname = lname, email = email, password=password, role=role)
        return Student.create(userID = user.userID, studentID = studentId, email = email, fname = fname, mname = mname, lname = lname, password = password, role = role)

    def createFaculty(self, fname: str, mname: str, lname: str, role: str = 'Faculty') -> Faculty:
        facultyId = self.getLastID(role) + 1
        password = lname + str(facultyId)
        email = "faculty" + str(facultyId) + "@elmwood.edu.ph"
        #checks if the email already exists
        if User.select().where(User.email == email).exists():
            raise ValueError(f"A user with the email {email} already exists.")
        #creates a user with the given email and password
        user = User.create(fname = fname, mname = mname, lname = lname, email = email, password=password, role=role)
        return Faculty.create(userID = user.userID, facultyID = facultyId, email = email, fname = fname, mname = mname, lname = lname, password = password, role = role)


    def createStaff(self, fname: str, mname: str, lname: str, role: str = 'Staff') -> Staff:
        staffId = self.getLastID(role) + 1
        password = lname + str(staffId)
        email = "staff" + str(staffId) + "@elmwood.edu.ph"
        #checks if the email already exists
        if User.select().where(User.email == email).exists():
            raise ValueError(f"A user with the email {email} already exists.")
        #creates a user with the given email and password
        user = User.create(fname = fname, mname = mname, lname = lname, email = email, password=password, role=role)
        return Staff.create(userID = user.userID, staffID = staffId, email = email, fname = fname, mname = mname, lname = lname, password = password, role = role)

    def createAdmin(self, email: str, password: str, fname: str = None, role: str = 'Admin'):
        #checks if the email already exists
        if User.select().where(User.email == email).exists():
            raise ValueError(f"A user with the email {email} already exists.")
        #creates a user with the given email and password
        user = User.create(fname = fname, email = email, password = password, role = role)
        #creates an admin with the given user
        return Admin.create(userID = user.userID, email = email, password = password, role='Admin')
    
    def createCourse(self, courseName: str) -> Course:
        if Course.select().where(Course.courseName == courseName).exists():
            raise ValueError(f"A course with the name {courseName} already exists.")
        return Course.create(courseName = courseName)
    
    def createSection(self, sectionName: str, courseName: str) -> Section:
        if Section.select().where(Section.sectionName == sectionName).exists():
            raise ValueError(f"A section with the name {sectionName} already exists.")
        
        try:
            course = Course.get(Course.courseName == courseName)
        except Course.DoesNotExist:
            raise ValueError(f"No course found with the name {courseName}")

        section = Section.create(sectionName = sectionName)
        CourseSection.create(courseID=course.courseID, sectionID=section.sectionID)

        return section

    def signIn(self, email: str, password: str):
        try:
            user = User.get(User.email == email, User.password == password)
            return user.role
        except User.DoesNotExist:
            print("Invalid email or password.")
            return "Invalid"
    

    def uploadDocument(self, email: str, filepath: str) -> UserDocuments:
        try:
            current_time = datetime.now().strftime("%Y%m%d%H%M%S")
            destination = "..\documents"
            subfolder_path = os.path.join(destination, current_time)
            os.mkdir(subfolder_path)
            new_filepath = shutil.copy2(filepath, subfolder_path)
            UserDocuments.create(email = email, documents = new_filepath)
            print(new_filepath)
        except Exception as e:
            return f"An error occurred while uploading the file: {str(e)}"

    #getters
    def getStudentByEmail(self, email: str):
        try:
            return Student.get(Student.email == email)
        except Student.DoesNotExist:
            return None

    def getStudentByID(self, studentID: str):
        try:
            return Student.get(Student.studentID == studentID)
        except Student.DoesNotExist:
            return None

    def getFacultyByID(self, facultyID: str):
        try:
            return Faculty.get(Faculty.facultyID == facultyID)
        except Faculty.DoesNotExist:
            return None
        
    def getFacultyByEmail(self, email: str):
        try:
            return Faculty.get(Faculty.email == email)
        except Faculty.DoesNotExist:
            return None   
        
    def getApplicantByID(self, applicantID: int):
        try:
            return Applicant.get(Applicant.applicantID == applicantID)
        except Applicant.DoesNotExist:
            return None
        
    def getCourseByName(self, courseName: str):
        try:
            return Course.get(Course.courseName == courseName)
        except Course.DoesNotExist:
            return None

    def displayAllSections(self, courseName: str):
        try:
            course = Course.get(Course.courseName == courseName)
        except Course.DoesNotExist:
            print(f"No course found with the name {courseName}")
            return

        course_sections = CourseSection.select().where(CourseSection.courseID == course.courseID)

        for course_section in course_sections:
            section = Section.get(Section.sectionID == course_section.sectionID)
            print(f"Section ID: {section.sectionID}, Section Name: {section.sectionName}")
        
    def getSectionByName(self, sectionName: str):
        try:
            return Section.get(Section.sectionName == sectionName)
        except Section.DoesNotExist:
            return None

    def getLastID(self, role):
        if role == "Student":
            # Get the current year
            current_year = datetime.now().year
            try:
                last_student_id = Student.select().order_by(Student.studentID.desc()).get().studentID
                return (current_year * 100000) + (last_student_id % 100000)
            except Student.DoesNotExist:
                return current_year * 100000  
        elif role == 'Faculty':
            try:
                return Faculty.select().order_by(Faculty.facultyID.desc()).get().facultyID
            except Faculty.DoesNotExist:
                return 0
        elif role == 'Staff':
            try:
                return Staff.select().order_by(Staff.staffID.desc()).get().staffID
            except Staff.DoesNotExist:
                return 0
        elif role == 'Admin':
            try:
                return Admin.select().order_by(Admin.adminID.desc()).get().adminID
            except Admin.DoesNotExist:
                return 0
        elif role == 'Applicant':
            try:
                return Applicant.select().order_by(Applicant.applicantID.desc()).get().applicantID
            except Applicant.DoesNotExist:
                return 0

    def removeUserByEmail(self, email: str):
        user = User.get(User.email == email)
        if user:
            if user.role == "Student":
                try:
                    student = Student.get(Student.userID == user.userID)
                    StudentSection.delete().where(StudentSection.studentID == student.studentID).execute()
                    StudentGrades.delete().where(StudentGrades.studentID == student.studentID).execute()
                    student.delete_instance()
                except Student.DoesNotExist:
                    pass  # No related Student record
            elif user.role == "Faculty":
                try:
                    faculty = Faculty.get(Faculty.userID == user.userID)
                    FacultySection.delete().where(FacultySection.facultyID == faculty.facultyID).execute()
                    faculty.delete_instance()
                except Faculty.DoesNotExist:
                    pass  # No related Faculty record
            elif user.role == "Staff":
                try:
                    staff = Staff.get(Staff.userID == user.userID)
                    staff.delete_instance()
                except Staff.DoesNotExist:
                    pass  # No related Staff record
            elif user.role == "Admin":
                try:
                    admin = Admin.get(Admin.userID == user.userID)
                    admin.delete_instance()
                except Admin.DoesNotExist:
                    pass  # No related Admin record
            elif user.role == "Applicant":
                try:
                    applicant = Applicant.get(Applicant.userID == user.userID)
                    applicant.delete_instance()
                except Applicant.DoesNotExist:
                    pass
            user.delete_instance()
            print(f"User {email} has been removed.")
        else:
            print("User not found.")
            
    #Admin Functions
    def displayAllCourses(self):
        courses = Course.select()
        for course in courses:
            print(f"Course ID: {course.courseID}, Course Name: {course.courseName}")

    def displayAllSections(self, courseName: str):
        try:
            course = Course.get(Course.courseName == courseName)
        except Course.DoesNotExist:
            print(f"No course found with the name {courseName}")
            return

        course_sections = CourseSection.select().where(CourseSection.courseID == course.courseID)

        for course_section in course_sections:
            section = Section.get(Section.sectionID == course_section.sectionID)
            print(f"Section ID: {section.sectionID}, Section Name: {section.sectionName}")

    def displayStudentGrades(self, studentID: int, facultyID: int = 0):
        if facultyID != 0:
            # Select sections that both studentID (StudentSection) and facultyID (FacultySection) have in common
            mutualSections = (Section
                                .select()
                                .join(StudentSection, on=(Section.sectionID == StudentSection.sectionID))
                                .where(StudentSection.studentID == studentID)
                                .switch(Section)
                                .join(FacultySection, on=(Section.sectionID == FacultySection.sectionID))
                                .where(FacultySection.facultyID == facultyID))
            grades = StudentGrades.select().where((StudentGrades.studentID == studentID) & (StudentGrades.sectionID.in_(mutualSections)))
            allSections = StudentSection.select().where(StudentSection.studentID == studentID)
            sectionIDsWithGrades = [grade.sectionID for grade in grades]
            sectionsWithoutGrades = [section for section in allSections if section.sectionID not in sectionIDsWithGrades and section.sectionID in mutualSections]
        else:
            grades = StudentGrades.select().where(StudentGrades.studentID == studentID)
            allSections = StudentSection.select().where(StudentSection.studentID == studentID)
            sectionIDsWithGrades = [grade.sectionID for grade in grades]
            sectionsWithoutGrades = [section for section in allSections if section.sectionID not in sectionIDsWithGrades]
        
        for studentSection in sectionsWithoutGrades:
            section = Section.get_or_none(Section.sectionID == studentSection.sectionID)
            if section is not None:
                print(f"Section Name: {section.sectionName}, No grade")

        for grade in grades:
            section = Section.get_or_none(Section.sectionID == grade.sectionID)
            if section is not None:
                sectionName = section.sectionName
                print(f"Section Name: {sectionName}, Grade: {grade.grades}")
            else:
                print(f"No section found for grade: {grade.grades}")
    
    def addFacultyToSection(self, facultyID: int, sectionName: str):
        faculty = Faculty.get(Faculty.facultyID == facultyID)
        section = Section.get(Section.sectionName == sectionName)

        if FacultySection.select().where((FacultySection.facultyID == faculty.facultyID) & (FacultySection.sectionID == section.sectionID)).exists():
            raise ValueError(f"The faculty {facultyID} is already assigned to the section {sectionName}.")

        return FacultySection.create(facultyID = faculty.facultyID, sectionID = section.sectionID)

    def addStudentToSection(self, studentID: int, sectionName: str):
        student = Student.get(Student.studentID == studentID)
        section = Section.get(Section.sectionName == sectionName)

        if StudentSection.select().where((StudentSection.studentID == student.studentID) & (StudentSection.sectionID == section.sectionID)).exists():
            raise ValueError(f"The student {studentID} is already assigned to the section {sectionName}.")

        return StudentSection.create(studentID = student.studentID, sectionID = section.sectionID)
    
    def displayAllStudents(self):
        students = Student.select()
        for student in students:
            print(f"Student ID: {student.studentID}, Student Name: {student.fname, student.mname, student.lname}, Student Email: {student.email}")

    def displayAllFaculty(self):
        faculties = Faculty.select()
        for faculty in faculties:
            print(f"Faculty ID: {faculty.facultyID}, Faculty Name: {faculty.fname, faculty.mname, faculty.lname}, Faculty Email: {faculty.email}")
    
    def displayAllApplicants(self):
        applicants = Applicant.select()
        for applicant in applicants:
            documents = UserDocuments.select().where(UserDocuments.email == applicant.email)
            print(f"Applicant ID: {applicant.applicantID}, Applicant Name: {applicant.fname, applicant.mname, applicant.lname}, Applicant Email: {applicant.email}")
            for document in documents:
                print(f"Submitted Document: {document.documents}")
            print("")
    
    def displayStudentDocuments(self, studentID: int):
        student = Student.get(Student.studentID == studentID)
        documents = UserDocuments.select().where(UserDocuments.email == student.email)
        for document in documents:
            print(f"Submitted Document: {document.documents}")
    
    #faculty functions
    def displayFacultyCourses(self, email: str):
        faculty = Faculty.get(Faculty.email == email)

        faculty_sections = FacultySection.select().where(FacultySection.facultyID == faculty.facultyID)

        for faculty_section in faculty_sections:
            section = Section.get(Section.sectionID == faculty_section.sectionID)
            course_section = CourseSection.get(CourseSection.sectionID == section.sectionID)
            course = Course.get(Course.courseID == course_section.courseID)
            print(f"Course: {course.courseName}, \nSection: {section.sectionName}")
            student_sections = StudentSection.select().where(StudentSection.sectionID == section.sectionID)

            for student_section in student_sections:
                student = Student.get(Student.studentID == student_section.studentID)
                print(f"Student: {student.studentID}, {student.fname, student.mname, student.lname}")

           

    def displayGrades(self, email: str):
        student = Student.get(Student.email == email)

        student_grades = StudentGrades.select().where(StudentGrades.studentID == student.studentID)

        for student_grade in student_grades:
            section = Section.get(Section.sectionID == student_grade.sectionID)
            course_section = CourseSection.get(CourseSection.sectionID == section.sectionID)
            course = Course.get(Course.courseID == course_section.courseID)

            print(f"Course: {course.courseName}, Section: {section.sectionName}, Grade: {student_grade.grades}")

    def gradeStudent(self, studentID: int, sectionID: int, grade: int):
        StudentGrades.create(studentID = studentID, sectionID = sectionID, grades = grade)
    
    def approveApplicant(self, applicantID: int):
        applicant = Applicant.get(Applicant.applicantID == applicantID)
        if applicant:
            fname = applicant.fname
            mname = applicant.mname
            lname = applicant.lname
            old_email = applicant.email

            student = self.createStudent(fname, mname, lname)
            UserDocuments.update(email=student.email).where(UserDocuments.email == old_email).execute()
            self.removeUserByEmail(old_email)
            print("Applicant successfully approved.")
        else:
            print(f'Applicant with ID {applicantID} not found.')
    
    def removeApplicant(self, applicantID: int):
        applicant = Applicant.get(Applicant.applicantID == applicantID)
        if applicant:
            self.removeUserByEmail(applicant.email)
            print("Applicant successfully removed.")
        else:
            print(f'Applicant with ID {applicantID} not found.')

    def getClassReport(self, sectionName: str):
        try:
            section = Section.get(Section.sectionName == sectionName)
            course_section = CourseSection.get(CourseSection.sectionID == section.sectionID)
            course = Course.get(Course.courseID == course_section.courseID)
        except Section.DoesNotExist:
            print(f"No section found with the name {sectionName}")
            return

        # Get all students from the section
        students = Student.select().join(StudentSection).where(StudentSection.sectionID == section.sectionID)

        print(f"{'Student ID':<15}{'First Name':<15}{'Middle Name':<15}{'Last Name':<15}{'Grade':<7}")
        print("-" * 67)
        for student in students:
            # Get the student's grade if it exists
            try:
                grade = StudentGrades.get((StudentGrades.studentID == student.studentID) & (StudentGrades.sectionID == section.sectionID))
                print(f"{student.studentID:<15}{student.fname:<15}{student.mname:<15}{student.lname:<15}{grade.grades:<7}")
            except StudentGrades.DoesNotExist:
                grade = "N/A"
                print(f"{student.studentID:<15}{student.fname:<15}{student.mname:<15}{student.lname:<15}{grade:<7}")