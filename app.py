from flask import Flask, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Prueba de despliegue para el proyecto de Infraestructura Virtual"

@app.route("/status")
def status():
    f=open("status.json", "r")
    data = f.read()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
