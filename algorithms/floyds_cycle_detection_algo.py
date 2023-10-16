"""
This is a cycle detection algorithm for Linked Lists.

Floyd's cycle finding algorithm or Hare-Tortoise algorithm is a pointer
algorithm that uses only two pointers, moving through the sequence at
different speeds. This algorithm is used to find a loop in a linked list.
It uses two pointers one moving twice as fast as the other one. The faster
one is called the fast pointer and the other one is called the slow pointer.

How Does Floyd's Cycle Finding Algorithm Works?

While traversing the linked list one of these things will occur:
- The Fast pointer may reach the end (NULL) this shows that there is no loop in the linked list.
- The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.
"""
