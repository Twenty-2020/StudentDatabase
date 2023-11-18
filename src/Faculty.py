from User import User
from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Faculty(User):
    facultyID = AutoField(null = False))
    userID = ForeignKeyField(User, to_field="userID", null = False))
    fname = CharField(null = False))
    mname = CharField()
    lname = CharField(null = False))
    email = CharField(unique = True, null = False))
    password = CharField(null = False))
    role = CharField(null = False))
    assignedSections = CharField(null = False))
