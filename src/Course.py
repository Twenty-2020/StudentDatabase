from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Course(BaseModel):
    courseID = AutoField()
    coursename = CharField()
