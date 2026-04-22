from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

FILE_DB = "files.json"

if not os.path.exists(FILE_DB):
    with open(FILE_DB, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return "Server running 🚀"

@app.route("/files", methods=["GET"])
def get_files():
    with open(FILE_DB, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/add-file", methods=["POST"])
def add_file():
    new_file = request.json

    with open(FILE_DB, "r") as f:
        data = json.load(f)

    data.append(new_file)

    with open(FILE_DB, "w") as f:
        json.dump(data, f, indent=2)

    return jsonify({"status": "success"})