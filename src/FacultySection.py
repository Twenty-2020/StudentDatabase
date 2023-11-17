from BaseModel import BaseModel
from peewee import *
from Faculty import Faculty
from Section import Section

db = SqliteDatabase('studentdatabase.db') 

class FacultySection(BaseModel):
    facultyID = ForeignKeyField(Faculty, to_field="facultyID")
    sectionID = ForeignKeyField(Section, to_field="sectionID")
