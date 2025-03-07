# Event Subscriber
class InventoryService:
    """Listens for events (orders) and reduce the product stock accordingly."""

    def notify(self, event_type, data=None):
        """Called when an event is published to the event bus.
        If product in order exists and stock>0, reduce stock."""
        if event_type == 'OrderPlaced':
            print(f"Inventory Updated: {data['product_name']} stock reduced by {data['quantity']}")
