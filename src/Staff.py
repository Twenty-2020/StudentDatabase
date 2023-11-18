from User import User
from BaseModel import BaseModel
from peewee import AutoField, ForeignKeyField, CharField

class Staff(User):
    staffID = AutoField(primary_key=True)
    user = ForeignKeyField(User, to_field="userID", backref='staff')
    fname = CharField()
    mname = CharField(null=True)  # Assuming middle name can be null
    lname = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()

# Assuming 'db' is the instance of SqliteDatabase
db.create_tables([Staff], safe=True)
