from peewee import *
from BaseModel import BaseModel

db = SqliteDatabase('studentdatabase.db') 

class User(BaseModel):
    userID = AutoField(null = False)
    fname = CharField(null = False)
    mname = CharField()
    lname = CharField(null = False)
    email = CharField(unique = True)
    password = CharField()
    role = CharField()

  
