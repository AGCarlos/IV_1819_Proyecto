from flask import Flask, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Prueba de despliegue para el proyecto de Infraestructura Virtual"

@app.route("/status")
def status():
    f=open("status.json", "r")
    data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
