import threading

from order_service import OrderService
from inventory_service import InventoryService
from notification_service import NotificationService
from event_bus import EventBus

def main():
    """Initialize EventBus and Start the services."""
    order_service = OrderService()
    inventory_service = InventoryService()
    notification_service = NotificationService()

    # Inventory and Notification listen
    EventBus.subscribe('OrderPlaced',inventory_service)
    EventBus.subscribe('OrderPlaced', notification_service)

    EventBus.is_sys_parallel()

    sys_parallel = EventBus.parallel_supported
    if sys_parallel:
        event_listening_thread = threading.Thread(target=EventBus.start_listening, daemon=True)
        event_listening_thread.start()

    # Create orders
    order_service.start()

    if sys_parallel:
        event_listening_thread.join()


if __name__ == "__main__":
    # Create
    main()