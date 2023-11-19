from BaseModel import BaseModel
from peewee import *
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file)

class Section(BaseModel):
<<<<<<< HEAD
    sectionID = AutoField(primary_key=True)
    sectionName = CharField()
=======
    sectionID = AutoField(null = False)
    sectionname = CharField(null = False)
>>>>>>> 420c6cb36a7a23c0c073f7f52ee241f203b04f84
