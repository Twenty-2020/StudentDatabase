from User import User
from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Applicant(User):
    applicantID = AutoField(null = False))
    fname = CharField(null = False))
    mname = CharField(null = False))
    lname = CharField(null = False))
    email = CharField(unique = True, null = False))
    uploadeddocs = CharField(null = False))
    role = CharField(null = False))

