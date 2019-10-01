from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_releated = BooleanField()
    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model)
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database

def create_and_conect():
    db.connect()
    db.create_tables([Person,Pet],safe = True)
    #El true es para que no colapse si la tabla ya esta creada

create_and_conect()