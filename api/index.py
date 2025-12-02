from flask import Flask, request, jsonify
from mangum import Mangum  # For AWS Lambda style integration
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route("/buy", methods=["POST"])
def buy():
    data = request.json
    return jsonify({"received": data})

# AWS Lambda handler
handler = Mangum(app)
