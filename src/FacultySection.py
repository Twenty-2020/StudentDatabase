from BaseModel import BaseModel
from Faculty import Faculty
from Student import Student
from Section import Section
from peewee import ForeignKeyField

class FacultySection(BaseModel):
    student = ForeignKeyField(Student, to_field="studentID", backref='faculty_sections')
    section = ForeignKeyField(Section, to_field="sectionID", backref='faculty_sections')

# ForeignKeyField(Student, to_field="studentID", backref='faculty_sections')`: Creates a foreign key relationship with the Student model.
# ForeignKeyField(Section, to_field="sectionID", backref='faculty_sections')`: Creates a foreign key relationship with the Section model.
# backref`: Creates a reverse relation in the Student and Section models so that you can access the associated faculty sections from a student or section instance.
