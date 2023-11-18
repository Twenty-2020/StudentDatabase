from BaseModel import BaseModel
from peewee import AutoField, CharField

class Section(BaseModel):
    sectionID = AutoField(primary_key=True)
    sectionname = CharField()

# Assuming 'db' is the instance of SqliteDatabase
db.create_tables([Section], safe=True)
