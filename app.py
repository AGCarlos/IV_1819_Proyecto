from flask import Flask, json, render_template
from fileS import *
import datetime


fl = FileDownload()

app = Flask(__name__)

@app.route("/")
def index():
    return "Buenos dias estamos en IV"

@app.route("/status")
def status():
    with open('status.json') as f:
        data = json.load(f)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/addFiles")
def add():

    data = {
    'id': '1',
    'nombre': 'https://i.ytimg.com/vi/ADYSC-5OWVM/maxresdefault.jpg',
    'path': 'pepe',
    'user': 'fernando',
    'fecha': str(datetime.datetime.now()),
    'type': 'img',
    'format': 'jpg',
    }

    r = redis.StrictRedis()
    r.execute_command('JSON.SET', 'doc', '.', json.dumps(data))
    reply = json.loads(r.execute_command('JSON.GET', 'doc'))
    return str(reply)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
