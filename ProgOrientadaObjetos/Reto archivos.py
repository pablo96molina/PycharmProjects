def agregar_articulo(articulo) :
    archivo_lista = open("lista.txt", "a")
    #agregar_articulo(input("Articulo que quieres agregar: "))

    archivo_lista.write("{}\n".format(articulo))

    archivo_lista.close()

def listar_articulos():
    archivo_lista = open("lista.txt", encoding="UTF-8")
    informacion = archivo_lista.read()
     #from archivo in archivo_lista:
    print(informacion)
    archivo_lista.close()

while True:
    print("Estas son las opciones que puedes seleccionar")
    print("1- Agregar articulo")
    print("2- Ver lista")
    print("3- Salir")

    operacion = int(input(": "))
    if operacion == 1:
        articulo = (input("Articulo que quieres agregar: "))
        agregar_articulo(articulo)
    elif operacion == 2:
        listar_articulos()
    else:
        break
