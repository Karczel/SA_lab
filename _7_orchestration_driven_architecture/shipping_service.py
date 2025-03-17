# Event Subscriber
class ShippingService:
    """Arrange Shipping the product."""
    def ship(self, order):
        print(f"Arranging shipping for Order ID {order['order_id']}")