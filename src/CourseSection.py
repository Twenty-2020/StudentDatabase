from BaseModel import BaseModel
from peewee import *
from Course import Course
from Section import Section
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)

class CourseSection(BaseModel):
    courseID = ForeignKeyField(Course, to_field="courseID", on_delete="CASCADE")
    sectionID = ForeignKeyField(Section, to_field="sectionID", on_delete="CASCADE")