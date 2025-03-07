# Event Subscriber
class NotificationService:
    """Listens for events (orders) and simulates sending email or notification."""

    def notify(self, event_type, data=None):
        """Called when an event is published to the event bus.
        Send notification for new order."""
        if event_type == 'OrderPlaced':
            print(f"Sending notification for Order ID: {data['order_id']} - {data['product_name']}")