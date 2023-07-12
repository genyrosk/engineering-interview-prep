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


if __name__ == "__main__":
    stack = Stack()

    print("stack size:", stack.size)
    print("stack size:", stack.is_empty)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)

    print("stack size:", stack.size)
    print("stack size:", stack.is_empty)

    el = stack.pop()
    print(el.value)
    el = stack.pop()
    print(el.value)
    el = stack.pop()
    print(el.value)
    el = stack.pop()
    print(el.value)
    el = stack.pop()
    print(el.value)
    el = stack.pop()
    print(el.value)
    try:
        el = stack.pop()
        print(el.value)
    except Exception as e:
        print("Exception:", e)

    print("stack size:", stack.size)
    print("stack size:", stack.is_empty)
