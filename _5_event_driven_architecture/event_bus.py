# Event Bus
import queue
import random


class EventBus:
    """Manages events and subscribers"""
    subscribers = {}
    event_queue = queue.Queue()
    listening_thread = None
    parallel_supported = random.choice([True, False])  # Randomly simulate parallel support

    @classmethod
    def subscribe(cls, event_type, subscriber):
        """Adds a subscriber to the list of consumers."""
        if event_type not in cls.subscribers:
            cls.subscribers[event_type] = []
        cls.subscribers[event_type].append(subscriber)

    @classmethod

    def is_sys_parallel(cls):
        if cls.parallel_supported:
            print("Sys support parallel computing")
        else:
            print("Sys doesn't support parallel computing")

    @classmethod
    def publish(cls, event_type, data=None):
        """Sends an event to all subscribers."""
        if cls.parallel_supported:
            cls.event_queue.put((event_type, data))
        else:
            if event_type in cls.subscribers:
                for subscriber in cls.subscribers[event_type]:
                    subscriber.notify(event_type, data)

    @classmethod
    def start_listening(cls):
        """Continuously listens for events in separate thread."""
        while True:
            event_type, data = cls.event_queue.get()
            if event_type in cls.subscribers:
                for subscriber in cls.subscribers[event_type]:
                    subscriber.notify(event_type, data)

