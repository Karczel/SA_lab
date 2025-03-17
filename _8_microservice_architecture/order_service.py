import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

class OrderService:
    def __init__(self):
        self.order_count = 123  # Start order count

    def create_order(self, user_id, product_id, quantity):
        """Creates an order."""

        # Proceed with order creation
        order = {
            "message": "Order created",
            "order_id": self.order_count,
            "customer_id": user_id,
            "product_id": product_id,
            "quantity": quantity
        }
        self.order_count += 1
        return order

order_service = OrderService()

@app.route("/orders", methods=["POST"])
def create_order():
    """Receives order details, checks inventory, and creates an order."""
    data = request.get_json()
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not all([user_id, product_id, quantity]):
        return jsonify({"error": "Missing data"}), 400

    order = order_service.create_order(user_id, product_id, quantity)
    response = {"message": "Order created", "order_id": order['order_id']}
    return jsonify(response), 201 if "error" not in order else 400

if __name__ == "__main__":
    app.run(port=5002, debug=True)
