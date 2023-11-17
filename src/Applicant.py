from User import User
from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Applicant(User):
    applicantID = AutoField()
    fname = CharField()
    mname = CharField()
    lname = CharField()
    email = CharField(unique = True)
    uploadeddocs = CharField()
    role = CharField()

