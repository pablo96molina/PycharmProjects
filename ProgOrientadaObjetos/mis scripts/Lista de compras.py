# Agregar Articulos
# Remover Articulos
# Ver Articulos

lista_articulos = list()


def agregar_articulo():
    articulo = input("Nombre del articulo a agregar: ")
    lista_articulos.append(articulo.capitalize())


def remover_articulo():
    articulo = input("Articulo a remover: ")
    lista_articulos.remove(articulo.capitalize())


def ver_articulo():
    for articulo in lista_articulos:
        print(articulo)


while True:
    print("Estas son las opciones que puedes seleccionar")
    print("1- Agregar articulo")
    print("2- Remover Articulos")
    print("3- Ver lista")
    print("4- Salir")

    operacion = int(input(": "))
    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulo()
    else:
        break

