import json
from flask import Flask ,render_template , redirect,request, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/<nombre>")
def hola_mundo(nombre="invitado"):
    contexto = {'nombre': nombre}
    return render_template("index.html", **contexto)

@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")

def suma(num1=0, num2=0):
    contexto = {'num1':num1, 'num2':num2}
    #Enumeras lo que tenes que pasar al html dentro de contexto
    #return render_template("suma.html",num1 = num1, num2 = num2) le lleva los valores al html
    return render_template("suma.html", **contexto)
@app.route("/contacto/")
def contacto():
    return render_template("contacto.html")

@app.route("/enviar/", methods=['POST'])
def enviar():
    response = redirect(url_for('hola_mundo'));
    response.set_cookie(json.dumps(dict(request.form.items())));
    return response

if __name__ == '__main__':
    app.run(debug=True)
