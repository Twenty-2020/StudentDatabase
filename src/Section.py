from BaseModel import BaseModel
from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class Section(BaseModel):
    sectionID = AutoField(null = False)
    sectionname = CharField(null = False)
