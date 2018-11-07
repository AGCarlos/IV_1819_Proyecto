from flask import Flask, json, render_template
from fileS import *
import datetime


fl = FileDownload()

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

@app.route("/addFiles")
def add():

jsonf = {
    "id": "1",
    "nombre": "pepe",
    "path": "https://i.ytimg.com/vi/ADYSC-5OWVM/maxresdefault.jpg",
    "user": "fernando",
    "fecha": str(datetime.datetime.now()),
    "type": "img",
    "format": "jpg"
}
#conectar a Redis y obtener el siguiente ID
r = redis.Redis()
cont = int(str(r.get("cont"))[2:-1])
fl.createFile(cont + 1,jsonf)

jsonf = r.get(2).decode('utf8').replace("'", '"')
# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(jsonf)
return json.dumps(data, indent=4, sort_keys=True)
response = app.response_class(
    response=json.dumps(data, indent=4, sort_keys=True),
    status=200,
    mimetype='application/json'
)
return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
