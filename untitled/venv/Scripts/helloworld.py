from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
#'/' significa la funcion principal o main

def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
@app.route('/images')
def hello_images():
    return "Hello images"

if __name__ =="__main__":
    app.run()
