from User import User
from BaseModel import BaseModel
from peewee import AutoField, ForeignKeyField, CharField, IntegerField

class Student(BaseModel):
    studentID = AutoField(primary_key=True)
    user = ForeignKeyField(User, to_field="userID", backref='students')
    fname = CharField()
    mname = CharField(null=True)  # Assuming middle name can be null
    lname = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()
    uploadeddocs = CharField()
    grades = IntegerField()
    enrolledSections = CharField()

# AutoField(primary_key=True): Automatically increments for each new record.
# ForeignKeyField(User, to_field="userID", backref='students'): Creates a foreign key relationship with the User model.
# CharField(unique=True): Ensures uniqueness of the email.
