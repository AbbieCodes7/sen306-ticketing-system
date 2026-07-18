# SEN 306 – Software Construction
## Tutor-Marked Assessment Report

**Name:** ABIGAIL OREVAOGHENE ASIEBA
**Matric No:** 2024/A/SENG/0059
**Email:** abigail.asieba@miva.edu.ng
**Department:** Software Engineering
---

## 1. Summary of Task

This project implements a **Customer Service Ticketing System** in Python to demonstrate the practical use of three core data structures: a Queue, a Stack, and a Singly Linked List. New support tickets are received and processed in the order they arrive using a **Queue**. Once a ticket has been handled, it is pushed onto a **Stack** so agents can review recently handled tickets, most recent first. Each individual ticket also maintains its own history of actions — such as creation, assignment, and status changes — using a **Singly Linked List**, allowing its full timeline to be traced from start to finish. The system is organized into four modules (`queue_module.py`, `stack.py`, `linkedlist.py`, and `main.py`), each responsible for a single, well-defined part of the application.

---

## 2. How Each Data Structure Was Used

### Queue (FIFO)
The Queue models the real-world behavior of a support desk: tickets must be handled in the order they were submitted, so the first customer to report an issue is the first to be helped. This is implemented in `queue_module.py` using Python's `collections.deque`, which allows efficient additions to the back (`enqueue`) and removals from the front (`dequeue`) without the performance cost of shifting elements, as would happen with a plain list. In `main.py`, all incoming tickets are placed into this queue and processed strictly in arrival order.

### Stack (LIFO)
The Stack models an agent's "recently viewed" list. After a ticket is processed, it is pushed onto the stack. When an agent wants to review recent activity, the most recently handled ticket is the first one they see (`pop`), which mirrors how humans naturally revisit the last thing they worked on. If this were implemented as a Queue instead, the agent would be shown the oldest processed ticket first, which is far less useful for a "recently viewed" feature. The Stack is implemented in `stack.py` using a Python list, with the end of the list treated as the "top."

### Singly Linked List
Each ticket needs to maintain a growing, ordered history of events (created → assigned → in progress → resolved). A Singly Linked List is well suited to this because history only ever grows at the end and is always read from the beginning to the most recent event — there is no need to access items randomly or move backward through the chain. Implemented in `linkedlist.py`, each `Node` stores an event description and a reference to the next node, and the `LinkedList` class tracks the `head` of the chain. Every `Ticket` object in `main.py` owns its own independent `LinkedList` instance to record its history.

---

## 3. Software Construction Principles Applied

**Modularity:** The application is split into four separate files, each with a single responsibility: `stack.py`, `queue_module.py`, and `linkedlist.py` each define one data structure, while `main.py` contains only the logic that ties them together into the ticketing workflow. This separation means any one module can be tested, reused, or modified independently of the others.

**High Cohesion:** Every method within each class performs exactly one clear task. For example, `is_empty()` in the Stack and Queue classes only checks whether the structure has items, and this single method is reused internally by both `pop()`/`peek()` and `dequeue()`/`peek()` rather than duplicating the same check in multiple places.

**Low Coupling:** `main.py` never accesses the internal data of any class directly (e.g., it never touches `Stack._items` or `LinkedList.head`). It interacts with each structure exclusively through public methods such as `enqueue()`, `push()`, and `append()`. This means the internal implementation of any data structure could be changed without requiring changes to `main.py`.

**Meaningful Naming:** Method names follow standard, widely recognized data structure vocabulary — `push`/`pop`/`peek` for the Stack, `enqueue`/`dequeue` for the Queue, and `append`/`traverse` for the Linked List — making the code immediately understandable to anyone familiar with these structures.

**Readability:** Every class and method includes a docstring explaining its purpose, consistent naming and indentation are used across all four files, and inline comments clarify non-obvious decisions, such as why `collections.deque` was chosen over a plain list for the Queue.

---

## 4. Conclusion

By combining a Queue, a Stack, and a Singly Linked List into a single cohesive ticketing system, this project demonstrates not only correct implementation of each data structure but also sound software construction practice: clear modular separation, single-responsibility methods, minimal interdependency between components, and consistent, readable code throughout.
