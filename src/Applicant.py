from User import User
from BaseModel import BaseModel
from peewee import *
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)

class Applicant(User):
<<<<<<< HEAD
    applicantID = AutoField(primary_key=True)
    userID = ForeignKeyField(User, to_field="userID", on_delete="CASCADE")

=======
    applicantID = AutoField(null = False)
    fname = CharField(null = False)
    mname = CharField()
    lname = CharField(null = False)
    email = CharField(unique = True)
    uploadeddocs = CharField()
>>>>>>> 420c6cb36a7a23c0c073f7f52ee241f203b04f84
