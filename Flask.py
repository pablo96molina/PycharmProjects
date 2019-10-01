from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hola_mundo(nombre="invitado"):
    nombre = request.args.get('nombre', nombre)
    #accedimos al request, despues a los argumentos, despues que obtenga el parametro con el nombre y lo asocie a la variable nombre
    return "Hola {}".format(nombre)
    #http://127.0.0.1:5000/?nombre=Pablo hay que poner el signo en el URL antes de la variable
@app.route("/images")
def hello_images():
    return "Hello Images"

if __name__ == '__main__':
    app.run(debug=True)
