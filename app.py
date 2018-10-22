from flask import Flask, json, render_template
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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
