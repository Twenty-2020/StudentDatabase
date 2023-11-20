from peewee import *
from BaseModel import BaseModel
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file) 

class User(BaseModel):
    userID = AutoField(primary_key=True)
    fname = CharField(null=True)
    mname = CharField(null=True)
    lname = CharField(null=True)
    email = CharField(unique = True, null = True)
    password = CharField(null = True)
    role = CharField()
