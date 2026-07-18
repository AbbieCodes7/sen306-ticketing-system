"""
stack.py

Implements a Stack (LIFO - Last In, First Out) data structure.
In the ticketing system, this is used to track recently viewed
tickets and to support undo functionality.
"""


class Stack:
    """A simple Stack implementation using a Python list internally."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items currently in the stack."""
        return len(self._items)

    def __str__(self):
        """Return a readable string representation of the stack (top last)."""
        return f"Stack({self._items})"