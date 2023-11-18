from User import User
from BaseModel import BaseModel
from peewee import AutoField, ForeignKeyField, CharField

class Faculty(User):
    facultyID = AutoField(primary_key=True)
    user = ForeignKeyField(User, to_field="userID", backref='faculties')
    fname = CharField()
    mname = CharField(null=True)  # Assuming middle name can be null
    lname = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()
    assignedSections = CharField()

# Assuming 'db' is the instance of SqliteDatabase
db.create_tables([Faculty], safe=True)
