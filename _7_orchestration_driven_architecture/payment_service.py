class PaymentService:
    """Process the payment."""
    def pay(self, order):
        print(f"Processing payment for Order {order['product_id']}, Quantity {order['quantity']}")
