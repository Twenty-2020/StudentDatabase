from peewee import *
from BaseModel import BaseModel

db = SqliteDatabase('studentdatabase.db') 

class User(BaseModel):
    userID = AutoField()
    fname = CharField()
    mname = CharField()
    lname = CharField()
    email = CharField(unique = True)
    password = CharField()
    role = CharField()

  
