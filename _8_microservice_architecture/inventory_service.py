from flask import Flask, request, jsonify

app = Flask(__name__)

class InventoryService:
    """Listens for events (orders) and reduces the product stock accordingly."""

    def __init__(self):
        self.product_stock = {
            '7': 100,
            '42': 50,
            '13': 25,
            '123': 102,
            '100': 10
        }

    def restock(self, product_id, quantity):
        """Restocks the specified product with the given quantity."""
        if product_id in self.product_stock:
            self.product_stock[product_id] += quantity
            return {"message": f"Restocked {product_id} by {quantity}. New stock: {self.product_stock[product_id]}"}
        return {"error": f"Product {product_id} not found."}, 404

    def restock_all(self):
        """Restocks all products with default values."""
        self.restock('7', 100)
        self.restock('42', 50)
        self.restock('13', 25)
        self.restock('30', 123)
        self.restock('100', 10)

    def check(self, order):
        """Called when an event is published to the event bus.
        If product in order exists and stock>0, reduce stock."""
        product_id = order["product_id"]
        quantity = order["quantity"]
        if product_id in self.product_stock:
            if self.product_stock[product_id] >= quantity:
                self.product_stock[product_id] -= quantity
                return {"message": "Product available", "stock" : self.product_stock[product_id]}
            return {"error": "Product available","stock" : {self.product_stock[product_id]}}, 400
        return {"error": f"Product {product_id} not found."}, 404

inventory_service = InventoryService()

@app.route("/inventory/check", methods=["POST"])
def check_inventory():
    """Handles order stock checking via API request."""
    order = request.json
    response = inventory_service.check(order)
    return jsonify(response), (200 if "message" in response else 400)

@app.route("/inventory/restock/<product_id>/<int:quantity>", methods=["POST"])
def restock_product(product_id, quantity):
    """Restocks a specific product."""
    response = inventory_service.restock(product_id, quantity)
    return jsonify(response), (200 if "message" in response else 404)

if __name__ == "__main__":
    app.run(port=5003, debug=True)
