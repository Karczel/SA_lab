import threading

from inventory_service import InventoryService
from payment_service import PaymentService
from shipping_service import ShippingService
from order_service import OrderService


class Orchestrator:
    def __init__(self):
        self.order_service = OrderService()
        self.payment_service = PaymentService()
        self.inventory_service = InventoryService()
        self.shipping_service = ShippingService()

    def run(self, user):
        self.process(100,5, user)
        self.process(30, 9, user)

    def process(self, product_id, quantity, user):
        # Create orders
        order = self.order_service.create_order(product_id, quantity, user)
        # payment
        self.payment_service.pay(order)
        # Check inventory
        self.inventory_service.check(order)
        # Shipping
        self.shipping_service.ship(order)
        # Success
        self.success(order)

    def success(self, order):
        print(f'Order {order["order_id"]} processed successfully! Shipping Status: Arranged')