# -*- coding: utf-8 -*-
from flask import Flask, json, render_template
from fileS import *
from flask import jsonify
import ast
import datetime

fl = FileDownload()
r = fl.conexion()

app = Flask(__name__)

@app.route("/")
def index():
    status = {
      "status": "OK",
      "ejemplo": {
        "ruta": "/ejemplo",
        "valor": "{ 'nombre': 'Carlos', 'datos': { 'edad': 1, 'cumpleaños': '15/5/97' } }"
      }
    }

    response = app.response_class(
        response=json.dumps(status),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/status")
def status():
    status = {
      "status": "OK",
      "ejemplo": {
        "ruta": "/ejemplo",
        "valor": "{ 'nombre': 'Carlos', 'datos': { 'edad': 1, 'cumpleaños': '15/5/97' } }"
      }
    }

    response = app.response_class(
        response=json.dumps(status),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/ejemplo")
def ejemplo():
    ejemplo = {
      "nombre": "Carlos",
      "datos": {
        "edad": 1,
        "cumpleaños": "15/5/97"
      }
    }

    response = app.response_class(
        response=json.dumps(ejemplo),
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
        response=json.dumps(dict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/addFiles")
def add():

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
    fl.createFile("file1",jsonf,r)

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
    fl.createFile("file2",jsonf,r)

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
    fl.createFile("file3",jsonf,r)

    response = app.response_class(
        response=json.dumps(jsonf),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True, use_reloader=True)
