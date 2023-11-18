from peewee import AutoField, CharField, ForeignKeyField
from User import User  
from BaseModel import BaseModel  

class Admin(User):
    adminID = AutoField(null=False)
    userID = ForeignKeyField(User, to_field="userID", null=False)
    fname = CharField(null=False)
    mname = CharField()
    lname = CharField(null=False)
    email = CharField(unique=True)
    password = CharField()
    role = CharField()

    class Meta:
        table_name = 'admin'
