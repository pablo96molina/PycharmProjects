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
        database = db
    #Siempre poner la clase Meta conectando con db

def create_and_conect():
    """Conecta la base de datos y crea las tablas"""
    db.connect()
    db.create_tables([Entry],safe=True)

create_and_conect()
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

def view_entries(search_query = None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print (timestamp)
        print ('+'*len(timestamp))
        print (entry.content)
        print("n) next entry")
        print ("q) return to menu")
        print ("d) delete entry")

        next_action = input("Action  ").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
def search_entries():
    """Search entries"""
    search_query = input("Search query ").strip()
    view_entries(search_query)
def delete_entry(entry):
    """Delete entry"""
    action = input("Are you sure? [Yn]").lower().strip()

    if action == 'y':
        entry.delete_instance()
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('d', delete_entry)
])

if __name__ == '__main__':
    menu_loop()
