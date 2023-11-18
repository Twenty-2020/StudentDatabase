from peewee import AutoField, CharField
from User import User  
from BaseModel import BaseModel  

class Applicant(User):
    applicantID = AutoField(null=False)
    fname = CharField(null=False)
    mname = CharField()
    lname = CharField(null=False)
    email = CharField(unique=True)
    uploadeddocs = CharField()
    role = CharField()

    class Meta:
        table_name = 'applicant'


