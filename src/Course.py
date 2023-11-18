from BaseModel import BaseModel
from peewee import Model, SqliteDatabase, AutoField, CharField

db = SqliteDatabase('studentdatabase.db')

class BaseModel(Model):
    class Meta:
        database = db

class Course(BaseModel):
    courseID = AutoField(null=False)
    coursename = CharField(null=False)
