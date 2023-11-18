from peewee import Model, SqliteDatabase

db = SqliteDatabase('studentdatabase.db')

class BaseModel(Model):
    class Meta:
        database = db
