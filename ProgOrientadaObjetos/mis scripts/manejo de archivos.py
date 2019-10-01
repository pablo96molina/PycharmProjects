import re
archivo = open("sample.txt", encoding="UTF-8")

informacion = archivo.read()

archivo.close()

print(informacion)