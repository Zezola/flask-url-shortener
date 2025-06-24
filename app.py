from flask import Flask, request, jsonify, render_template
import uuid

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({'name': 'Pedro'})

@app.route("/url", methods=['GET','POST'])
def add_url():
    return render_template('index.html')