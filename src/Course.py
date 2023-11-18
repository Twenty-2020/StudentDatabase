from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Course(BaseModel):
    courseID = AutoField(null = False))
    coursename = CharField(null = False))
