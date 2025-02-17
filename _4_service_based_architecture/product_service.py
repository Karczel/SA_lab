from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.get_json()
    product_name = data.get("product_name")

    if not product_name:
        return jsonify({"error": "Product name is required"}), 400

    if product_name in products:
        return jsonify({"error": "Product already exists"}), 400

    products.append(product_name)
    return jsonify({"message": "Product added successfully"}), 201


@app.route("/get_products", methods=["GET"])
def get_products():
    all_products = []
    for i in range(len(products)):
        all_products.append({"product_id": i+1, "product_name": products[i]})
    return jsonify({"products" : all_products}), 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)