from flask import Flask
#from flask import request

app = Flask(__name__)

@app.route("/")
@app.route("/<nombre>")
def hola_mundo(nombre="invitado"):
    #nombre = request.args.get('nombre', nombre)
    #accedimos al request, despues a los argumentos, despues que obtenga el parametro con el nombre y lo asocie a la variable nombre
    return "Hola {}".format(nombre)
    #http://127.0.0.1:5000/?nombre=Pablo hay que poner el signo en el URL antes de la variable

@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")

def suma(num1 = 0, num2 = 0):
    #num1 = request.args.get('num1', num1)
    #num2 = request.args.get('num2', num2)
    #return "{} más {} es igual a {}".format(num1,num2, num1 + num2 )
    return """
    <!doctype html>
    <html>
        <head>
        <title> Suma </title>
        </head>
        
        <body>
        <h1>"{} más {} es igual a {}"</h1>
        
        </body>
    </html>
    """.format(num1,num2, num1 + num2 )
if __name__ == '__main__':
    app.run(debug=True)
