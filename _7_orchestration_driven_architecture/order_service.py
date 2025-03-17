class OrderService:
    order_count = 1234

    def create_order(self, product_id, quantity, user):
        """Simulates order creation and publishes an order event to the eventbus."""
        order = {
            "customer" : user,
            "order_id": self.order_count,
            "product_id": product_id,
            "quantity": quantity
        }
        print(f"Order Created: Customer ID {user.id}, Product ID {id}, Quantity {quantity}")
        self.order_count += 1

        return order