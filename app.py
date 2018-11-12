from flask import Flask, json, render_template
from fileS import *
from flask import jsonify
import datetime

fl = FileDownload()
r = fl.conexion("d")

app = Flask(__name__)

@app.route("/")
def status():
    with open('status.json') as f:
        data = json.load(f)

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/ejemplo")
def ejemplo():
    with open('ejemplo.json') as f:
        data = json.load(f)

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/archivos/<archivo>")
def muestraArchivos(archivo):
    dict = str(r.hgetall(archivo)).replace(' b',' ')
    dict = dict.replace('b','',1)[1:-1]
    jsonf = json.dumps(dict)
    jsonf2 = json.loads(jsonf)
    return jsonify(jsonf2)

@app.route("/addFiles")
def add():

    jsonf = {
        "id": "1",
        "nombre": "file",
        "path": "https://i.ytimg.com/vi/Yp7L1GHaZLI/maxresdefault.jpg",
        "user": "Carlos",
        "fecha": str(datetime.datetime.now()),
        "type": "img",
        "format": "jpg"
    }
    #Conectar a Redis para añadir la información
    fl.createFile("file",jsonf)

    dict = str(r.hgetall("file")).replace(' b',' ')
    dict = dict.replace('b','',1)[1:-1]
    jsonf = json.dumps(dict)
    jsonf2 = json.loads(jsonf)
    return jsonify(jsonf2)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
