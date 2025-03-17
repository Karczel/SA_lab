# Event Publisher
from event_bus import EventBus

class OrderService:
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
        self.create_order("Soap", 0)
        self.create_order("Shampoo", 10)
        self.create_order("Soap", 100)
        self.create_order("Face Cleanser", 5)
        self.create_order("Soap", 5)
        self.create_order("Bath Bomb", 8)
        self.create_order("Bath Bomb", 5)
