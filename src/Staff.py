from User import User
from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Staff(User):
    staffID = AutoField(null = False)
    userID = ForeignKeyField(User, to_field="userID", null = False)
    fname = CharField(null = False)
    mname = CharField()
    lname = CharField(null = False)
    email = CharField(unique = True)
    password = CharField()
    role = CharField()
