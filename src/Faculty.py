from User import User
from BaseModel import BaseModel
from peewee import *
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)

class Faculty(User):
<<<<<<< HEAD
    facultyID = AutoField(primary_key=True)
    userID = ForeignKeyField(User, to_field="userID", on_delete="CASCADE")

=======
    facultyID = AutoField(null = False)
    userID = ForeignKeyField(User, to_field="userID", null = False)
    fname = CharField(null = False)
    mname = CharField()
    lname = CharField(null = False)
    email = CharField(unique = True)
    password = CharField()
    role = CharField()
    assignedSections = CharField()
>>>>>>> 420c6cb36a7a23c0c073f7f52ee241f203b04f84
