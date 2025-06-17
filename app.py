from flask import Flask

app = Flask(__name__)

# Por enquanto vamos guardar as URLs em memória em um JSON

@app.route("/")
def index():
    return "<p>Hello</p>"

