from BaseModel import BaseModel
from peewee import Model, SqliteDatabase, ForeignKeyField
from Course import Course
from Section import Section

db = SqliteDatabase('studentdatabase.db')

class BaseModel(Model):
    class Meta:
        database = db

class CourseSection(BaseModel):
    courseID = ForeignKeyField(Course, to_field="courseID")
    sectionID = ForeignKeyField(Section, to_field="sectionID")
