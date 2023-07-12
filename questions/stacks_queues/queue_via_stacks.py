"""
3.4 Queue via Stacks

Implement a Queue class using 2 stacks
"""


class Node:
    def __init__(self, value: any, next_node):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self):
        self.size = 0
        self.last = None

    def push(self, value: any):
        self.size += 1
        node = Node(value, self.last)
        self.last = node

    def pop(self) -> any:
        if not self.last:
            raise Exception("Stack is empty")
        self.size -= 1
        popped = self.last
        self.last = self.last.next
        return popped

    @property
    def is_empty(self):
        return not self.last


class Queue:
    def __init__(self):
        self.stack_one
        self.stack_two

    def push(self):
        pass

    def pop(self):
        pass


if __name__ == "__main__":
    q = Queue()
