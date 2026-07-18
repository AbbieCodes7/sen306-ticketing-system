"""
main.py

Demonstrates the Customer Service Ticketing System.
Integrates Stack, Queue, and Singly Linked List to simulate
how support tickets are received, processed, and tracked.
"""

from stack import Stack
from queue_module import Queue
from linkedlist import LinkedList


class Ticket:
    """Represents a single support ticket with its own action history."""

    def __init__(self, ticket_id, subject):
        self.ticket_id = ticket_id
        self.subject = subject
        self.history = LinkedList()  # each ticket has its own event chain
        self.history.append(f"Ticket #{ticket_id} created: '{subject}'")

    def add_event(self, event):
        """Record a new event in this ticket's history."""
        self.history.append(event)

    def __str__(self):
        return f"Ticket #{self.ticket_id} - {self.subject}"


def main():
    # Queue holds new tickets waiting to be handled (FIFO)
    ticket_queue = Queue()

    # Stack holds recently viewed/processed tickets (LIFO)
    recently_viewed = Stack()

    # --- Simulate new tickets arriving ---
    ticket_queue.enqueue(Ticket(1, "Cannot log into account"))
    ticket_queue.enqueue(Ticket(2, "Payment not going through"))
    ticket_queue.enqueue(Ticket(3, "App crashes on startup"))

    print("Tickets waiting in queue:", ticket_queue.size())
    print("-" * 40)

    # --- Process tickets one by one, in the order they arrived ---
    while not ticket_queue.is_empty():
        current_ticket = ticket_queue.dequeue()
        print(f"Processing: {current_ticket}")

        # Record events in this ticket's own history (linked list)
        current_ticket.add_event(f"Assigned to Agent Dara")
        current_ticket.add_event(f"Status changed to In Progress")
        current_ticket.add_event(f"Status changed to Resolved")

        # Push to the "recently viewed" stack once handled
        recently_viewed.push(current_ticket)

        # Show this ticket's full history
        print("  History:", current_ticket.history.traverse())
        print()

    print("-" * 40)
    print("All tickets processed. Queue is now empty:", ticket_queue.is_empty())

    # --- Demonstrate the stack: agent reviews recently handled tickets ---
    print("\nAgent reviews recently handled tickets (most recent first):")
    while not recently_viewed.is_empty():
        ticket = recently_viewed.pop()
        print(f"  Reviewed: {ticket}")

    print("\nRecently viewed stack is now empty:", recently_viewed.is_empty())


if __name__ == "__main__":
    main()