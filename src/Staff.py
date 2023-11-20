from User import User
from BaseModel import BaseModel
from peewee import *
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file) 

class Staff(User):
    staffID = AutoField(null = False)
    userID = ForeignKeyField(User, to_field="userID", null = False)
    fname = CharField(null = False)
    mname = CharField()
    lname = CharField(null = False)
    email = CharField(unique = True)
    password = CharField()
    role = CharField()
