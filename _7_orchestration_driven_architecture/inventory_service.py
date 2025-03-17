# Event Subscriber
class InventoryService:
    """Listens for events (orders) and reduce the product stock accordingly."""

    def __init__(self):
        self.product_stock = {
            '7': 100,
            '42': 50,
            '13': 25,
            '100': 10
        }

    def restock(self, product_name, quantity):
        """Restocks the specified product with the given quantity."""
        if product_name in self.product_stock:
            self.product_stock[product_name] += quantity
            print(f"Restocked: {product_name} by {quantity}. New stock: {self.product_stock[product_name]}")
        else:
            print(f"Inventory Error: Product {product_name} not found.")

    def restock_all(self):
        self.restock('Soap', 100)
        self.restock('Shampoo', 50)
        self.restock('Face Cleanser', 25)
        self.restock('Bath Bomb', 10)

    def check(self, order):
        """Called when an event is published to the event bus.
        If product in order exists and stock>0, reduce stock."""
        product_id = order["product_id"]
        quantity = order["quantity"]
        if product_id in self.product_stock:
            if self.product_stock[product_id] >= quantity:
                self.product_stock[product_id] -= quantity
                print(f"Checking inventory for Product ID {product_id} Quantity {quantity}")
            else:
                print(
                    f"Inventory Error: Not enough stock for {product_id}. Current stock: {self.product_stock[product_id]}")
        else:
            print(f"Inventory Error: Product {product_id} not found.")

