from BaseModel import BaseModel
from Student import Student
from Section import Section
from peewee import ForeignKeyField

class FacultySection(BaseModel):
    student = ForeignKeyField(Student, to_field="studentID", backref='faculty_sections')
    section = ForeignKeyField(Section, to_field="sectionID", backref='faculty_sections')

db.create_tables([FacultySection], safe=True)
