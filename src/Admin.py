from User import User
from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Admin(User):
    adminID = AutoField()
    userID = ForeignKeyField(User, to_field="userID")
    fname = CharField()
    mname = CharField()
    lname = CharField()
    email = CharField(unique = True)
    password = CharField()
    role = CharField()
