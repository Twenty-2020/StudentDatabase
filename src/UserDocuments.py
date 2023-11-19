from BaseModel import BaseModel
from peewee import *
from User import User
import os
# Get the parent directory of the current script
parent_dir = os.path.dirname(os.getcwd())

# Create the .db file in the parent directory
db_file = os.path.join(parent_dir, 'studentdatabase.db')
db = SqliteDatabase(db_file) 

class UserDocuments(BaseModel):
    email = ForeignKeyField(User, to_field="email", on_delete="CASCADE")
    documents = CharField(null = True)