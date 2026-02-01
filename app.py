from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "Backend running successfully"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({
        "prediction": "Not Hate Speech",
        "confidence": 90
    })

if __name__ == "__main__":
    app.run()
