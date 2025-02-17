import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

WEB_PROTOCOL = "http://"

HOST_URL = "127.0.0.1"

USER_MANAGEMENT_PORT = "5001"
PRODUCT_MANAGEMENT_PORT = "5002"

USER_SERVICE_URL = f"{WEB_PROTOCOL}{HOST_URL}:{USER_MANAGEMENT_PORT}"
PRODUCT_SERVICE_URL = f"{WEB_PROTOCOL}{HOST_URL}:{PRODUCT_MANAGEMENT_PORT}"

@app.route("/register_user", methods=["POST"])
def register_user():
    response = requests.post(f"{USER_SERVICE_URL}/register", json=request.get_json())
    return jsonify(response.json()), response.status_code


@app.route("/login_user", methods=["POST"])
def login_user():
    response = requests.post(f"{USER_SERVICE_URL}/login", json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route("/add_product", methods=["POST"])
def add_product():
    response = requests.post(f"{PRODUCT_SERVICE_URL}/add_product", json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route("/get_products", methods=["GET"])
def get_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/get_products")
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000, debug=True)