from BaseModel import BaseModel
from peewee import *
from Student import Student
from Section import Section

db = SqliteDatabase('studentdatabase.db') 

class FacultySection(BaseModel):
    studentID = ForeignKeyField(Student, to_field="studentID")
    sectionID = ForeignKeyField(Section, to_field="sectionID")
