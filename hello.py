from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Mundo!, Este es el ambiente de QA"