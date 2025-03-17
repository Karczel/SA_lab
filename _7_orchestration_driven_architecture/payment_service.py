class PaymentService:
    """Process the payment."""
    def pay(self, order):
        print(f"Processing payment for Order ID {order['order_id']}")
