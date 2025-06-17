from flask import Flask, request, jsonify

app = Flask(__name__)

# Por enquanto vamos guardar as URLs em memória em um JSON

@app.route("/")
def index():
    return jsonify({'name': 'Pedro'})

@app.route("/url", methods=['POST'])
def add_url():
    data = request.get_json()
    url = data['url']
    return jsonify(url)