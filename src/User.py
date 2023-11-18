from peewee import Model, SqliteDatabase, AutoField, CharField

db = SqliteDatabase('studentdatabase.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    userID = AutoField(primary_key=True)
    fname = CharField()
    mname = CharField()
    lname = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()
