from peewee import *

db = SqliteDatabase('studentdatabase.db') 

class BaseModel(Model):
    class Meta:
        database = db
