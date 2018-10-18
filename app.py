from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Prueba de despliegue para el proyecto de Infraestructura Virtual"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
