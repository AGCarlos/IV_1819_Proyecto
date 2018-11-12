from flask import Flask, json, render_template
from fileS import *
from flask import jsonify
import ast
import datetime

fl = FileDownload()
r = fl.conexion()

app = Flask(__name__)

@app.route("/")
def status():
    dict = str(r.hgetall("status")).replace(' b',' ')
    dict = dict.replace('b','',1)
    dict = ast.literal_eval(dict)

    response = app.response_class(
        response=json.dumps(dict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/ejemplo")
def ejemplo():
    dict = str(r.hgetall("ejemplo")).replace(' b',' ')
    dict = dict.replace('b','',1)
    dict = ast.literal_eval(dict)

    response = app.response_class(
        response=json.dumps(dict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/archivos/<archivo>")
def muestraArchivos(archivo):
    dict = str(r.hgetall(archivo)).replace(' b',' ')
    dict = dict.replace('b','',1)
    dict = ast.literal_eval(dict)

    response = app.response_class(
        response=json.dumps(dict ),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/addFiles")
def add():

    jsonf = {
      "status": "OK",
      "ejemplo": {
        "ruta": "/ejemplo",
        "valor": "{ 'nombre': 'Carlos', 'datos': { 'edad': 1, 'cumpleaños': '15/5/97' } }"
      }
    }
    #Conectar a Redis para añadir la información
    fl.createFile("status",jsonf)

    jsonf = {
      "nombre": "Carlos",
      "datos": {
        "edad": 1,
        "cumpleaños": "15/5/97"
      }
    }
    #Conectar a Redis para añadir la información
    fl.createFile("ejemplo",jsonf)

    jsonf = {
        "id": "1",
        "nombre": "file1",
        "path": "https://i.ytimg.com/vi/Yp7L1GHaZLI/maxresdefault.jpg",
        "user": "Carlos",
        "fecha": str(datetime.datetime.now()),
        "type": "img",
        "format": "jpg"
    }
    #Conectar a Redis para añadir la información
    fl.createFile("file1",jsonf)

    jsonf = {
        "id": "2",
        "nombre": "file2",
        "path": "https://i.ytimg.com/vi/Yp7L1GHaZLI/maxresdefault.jpg",
        "user": "Carlos",
        "fecha": str(datetime.datetime.now()),
        "type": "img",
        "format": "jpg"
    }
    #Conectar a Redis para añadir la información
    fl.createFile("file2",jsonf)

    jsonf = {
        "id": "3",
        "nombre": "file3",
        "path": "https://i.ytimg.com/vi/Yp7L1GHaZLI/maxresdefault.jpg",
        "user": "Wendousa",
        "fecha": str(datetime.datetime.now()),
        "type": "img",
        "format": "jpg"
    }
    #Conectar a Redis para añadir la información
    fl.createFile("file3",jsonf)

    response = app.response_class(
        response=json.dumps(jsonf),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
