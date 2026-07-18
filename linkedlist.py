"""
linked-list.py

Implements a Singly Linked List data structure.
In the ticketing system, this is used to represent the
chronological history of events/actions on a ticket.
"""


class Node:
    """A single node in the linked list, holding data and a reference to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self._size = 0

    def append(self, data):
        """Add a new node containing data to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._size += 1

    def remove(self, data):
        """
        Remove the first node whose data matches the given value.
        Returns True if a node was removed, False if not found.
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def traverse(self):
        """Return a list of all data items in order, from head to tail."""
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def is_empty(self):
        """Return True if the list has no nodes, False otherwise."""
        return self.head is None

    def size(self):
        """Return the number of nodes in the list."""
        return self._size

    def __str__(self):
        """Return a readable string representation of the list."""
        return f"LinkedList({self.traverse()})"