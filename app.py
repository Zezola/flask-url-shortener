from flask import Flask, request, jsonify

app = Flask(__name__)

# Por enquanto vamos guardar as URLs em memória em um JSON
url_db = {
    "aBc1": "https://www.google.com/",
    "xYz9": "https://docs.python.org/3/"
}

@app.route("/")
def index():
    return jsonify({'name': 'Pedro'})

@app.route("/url", methods=['POST'])
def add_url():
    data = request.get_json()
    url = data['url']
    if not url:
        return jsonify({"erro": "URL não fornecida"}), 400
    codigo_curto = "testeExemplo"
    url_db[codigo_curto] = url
    url_curta = request.host_url + codigo_curto
    return jsonify({
        "url_original": url,
        "url_curta": url_curta
    })