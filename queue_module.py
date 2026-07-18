"""
queue_module.py

Implements a Queue (FIFO - First In, First Out) data structure.
In the ticketing system, this is used to hold new tickets waiting
to be handled, in the order they arrived.
"""

from collections import deque


class Queue:
    """A simple Queue implementation using collections.deque internally."""

    def __init__(self):
        """Initialize an empty queue."""
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        Returns None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        return self._items.popleft()

    def peek(self):
        """
        Return the front item without removing it.
        Returns None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self._items[0]

    def is_empty(self):
        """Return True if the queue has no items, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items currently in the queue."""
        return len(self._items)

    def __str__(self):
        """Return a readable string representation of the queue (front first)."""
        return f"Queue({list(self._items)})"