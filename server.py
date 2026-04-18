from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

FILE_DB = "files.json"

# Ensure file exists
if not os.path.exists(FILE_DB):
    with open(FILE_DB, "w") as f:
        json.dump([], f)

# 📥 GET all files
@app.route("/files", methods=["GET"])
def get_files():
    try:
        with open(FILE_DB, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify([])

# 📤 ADD new file
@app.route("/add-file", methods=["POST"])
def add_file():
    try:
        new_file = request.json

        with open(FILE_DB, "r") as f:
            data = json.load(f)

        data.append(new_file)

        with open(FILE_DB, "w") as f:
            json.dump(data, f, indent=2)

        return jsonify({"status": "success"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# 🔥 HEALTH CHECK (important for deployment)
@app.route("/")
def home():
    return "Server is running 🚀"

if __name__ == "__main__":
    app.run(debug=True)