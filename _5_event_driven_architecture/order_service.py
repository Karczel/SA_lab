# Event Publisher
from event_bus import EventBus

class OrderService:
    """Singleton"""
    order_count = 0

    def create_order(self, name, quantity):
        """Simulates order creation and publishes an order event to the eventbus."""
        order = {
            "order_id": self.order_count,
            "product_name": name,
            "quantity": quantity
        }
        print(f"Order Created{order}")
        self.order_count += 1

        EventBus.publish('OrderPlaced', order)

    def start(self):
        """Starts the order creation process and emits events."""
        self.create_order("Product-0", 0)
        self.create_order("Product-1", 10)
        # Todo: Add products
