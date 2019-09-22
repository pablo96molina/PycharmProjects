from peewee import *
import datetime
import  sys

from collections import OrderedDict
db = SqliteDatabase("diary.db")


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
            print("{}, {}".format(key,value.__doc__)),
            #value.__doc__ significa que se imprimira el """texto""" de la funcion
        choice = input("Actions ").lower().strip()

        if choice in menu:
            menu[choice]()
        #Esto ejecuta la opcion seleccionada, porque choice pasa a ser una de las opciones (letras) ingresadas,
        # entonces ejecuta la funcion asociada a esa letra
        # el if habilita las opciones que fuieron definidas en menu, sino salta error
def add_entry():
    """Add entry"""
    print("Enter your thoughts. Press ctrl + Z to finish")
    data = sys.stdin.read().strip()
    if data:
        #comprueba que data no este vacio
       Entry.create(content=data)
        #Carga en una linea el contenido de data

def view_entries():
    """View all entries"""
    entries = entries.select().order_by(entry.timestamp.desc())
    for entry in entries:
        timestamp = entry.timestamp.strtime()

def delete_entry(Entry):
    """Delete entry"""





menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('d', delete_entry)
])

if __name__ == '__main__':
    menu_loop()