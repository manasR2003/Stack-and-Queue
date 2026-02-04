🔹 Stack (LIFO – Last In First Out)

A Stack is a linear data structure that follows the Last In First Out (LIFO) principle.
In this implementation, the stack is created using a singly linked list, where insertion and deletion happen at the head node.

Key Operations:

push() – Inserts an element at the top of the stack

pop() – Removes and returns the top element

peek() – Returns the top element without removing it

isEmpty() – Checks whether the stack is empty

stackSize() – Returns the number of elements in the stack

Advantages:

Dynamic size (no fixed limit like arrays)

Efficient push and pop operations → O(1) time complexity

Use Cases:

Function calls (call stack)

Undo/Redo operations

Expression evaluation

Backtracking algorithms

🔹 Queue (FIFO – First In First Out)

A Queue is a linear data structure that follows the First In First Out (FIFO) principle.
This queue is implemented using a linked list with two pointers: front and rear.

Key Operations:

enqueue() – Inserts an element at the rear of the queue

dequeue() – Removes and returns the front element

peek() – Returns the front element without removing it

isEmpty() – Checks whether the queue is empty

size() – Returns the total number of elements

Advantages:

No overflow issues due to dynamic memory allocation

Constant time insertion and deletion → O(1)

Use Cases:

CPU scheduling

Task/Job scheduling

Printer queues

Data buffering

🔹 Why Linked List Implementation?

No need for contiguous memory

Efficient insertion and deletion

Better memory utilization for dynamic data

🔹 Time Complexity
Operation	Stack	Queue
Insert	O(1)	O(1)
Delete	O(1)	O(1)
Peek	O(1)	O(1)
🔹 Technologies Used

Python

Object-Oriented Programming (OOP)

Linked List Data Structure

What is a Linked List?

A Linked List is a linear data structure where elements (called nodes) are stored in non-contiguous memory locations.
Each node contains:

Data

Reference (pointer) to the next node

Structure of a Node

data → stores the value

next → points to the next node in the list

The last node points to NULL

Types of Linked Lists

Singly Linked List – each node points to the next node

Doubly Linked List – nodes have previous and next pointers

Circular Linked List – last node points back to the first node

Basic Operations

Insertion (at beginning, end, or specific position)

Deletion (from beginning, end, or specific node)

Traversal (displaying elements)

Searching an element

Finding minimum / maximum value

Reversing the list

Advantages

Dynamic size (no fixed memory)

Efficient insertions and deletions

No memory wastage like arrays

Disadvantages

No direct access to elements (no indexing)

Extra memory required for pointers

Slower access compared to arrays

Time Complexity
Operation	Time Complexity
Access	O(n)
Search	O(n)
Insertion	O(1)*
Deletion	O(1)*

* When position/node is already known
