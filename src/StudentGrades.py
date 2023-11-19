from BaseModel import BaseModel
from peewee import *
from Student import Student
from Section import Section
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file) 

class StudentGrades(BaseModel):
    studentID = ForeignKeyField(Student, to_field="studentID", on_delete="CASCADE")
    sectionID = ForeignKeyField(Section, to_field="sectionID", on_delete="CASCADE")
    grades = CharField(null = True)