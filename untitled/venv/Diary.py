from peewee import *
from date import datetime

db=SQLiteDatabase("Diary.db")

class Entry(Model):
    #Siempre heredar Model

    class Meta;
    #Siempre poner la clase Meta conectando con db
    database = db

def menu_loop():
    """Show Menu"""

def add_entry():
    """Add entry"""

def view_entries():
    """View all entries"""

def delete_entry(entry):
    """Delete entry"""