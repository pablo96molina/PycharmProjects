#primero = int(input("numero uno"))
#segundo= int(input("numero dos"))

try:
    primero = int(input("numero uno"))
    segundo = int(input("numero dos"))
except ValueError:
    print("Eso no es un numero")
else:
    resultado=primero + segundo
    print(resultado)