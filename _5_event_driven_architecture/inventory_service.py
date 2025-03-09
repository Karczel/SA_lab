# Event Subscriber
class InventoryService:
    """Listens for events (orders) and reduce the product stock accordingly."""

    def __init__(self):
        self.product_stock = {
            'Soap': 100,
            'Shampoo': 50,
            'Face Cleanser': 25,
            'Bath Bomb': 10
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

    def notify(self, event_type, data=None):
        """Called when an event is published to the event bus.
        If product in order exists and stock>0, reduce stock."""
        if event_type == 'OrderPlaced':
            product_name = data['product_name']
            quantity = data['quantity']

            if product_name in self.product_stock:
                if self.product_stock[product_name] >= quantity:
                    self.product_stock[product_name] -= quantity
                    print(f"Inventory Updated: {data['product_name']} stock reduced by {data['quantity']}")
                else:
                    print(
                        f"Inventory Error: Not enough stock for {product_name}. Current stock: {self.product_stock[product_name]}")
            else:
                print(f"Inventory Error: Product {product_name} not found.")

