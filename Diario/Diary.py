from peewee import *
import datetime
from collections import OrderedDict
db = SqliteDatabase("diary.db")


menu = OrderedDict([
    ('a','add entry'),
    ('v','view entry'),
    ('d','delete entry')
])
class Entry(Model):
#Siempre heredar Model
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
    #Siempre poner la clase Meta conectando con db
        database = db
def create_and_conect():
    """Conecta la base de datos y crea las tablas"""
    db.conect()
    db.create_tables([Entry])
def menu_loop():
    """Show Menu"""
    choice = None
    while choice != 'q':
        print("Press q to quit")
        for key,value in menu.items():
            print("{}, {}".format(key,value)),
        choice = input("Actions ").lower().strip()


def add_entry():
    """Add entry"""


def view_entries():
    """View all entries"""


def delete_entry(Entry):
    """Delete entry"""


if __name__ == '__main__':
    menu_loop()

