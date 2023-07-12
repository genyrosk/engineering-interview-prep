"""
3.3 Stack of Plates
-------------------

Imagine a stack of plates. If the stack gets too high, it might topple.
Therefore in real life you would likely start a new stack when the
precious stack exceeds some thresdhold.
Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a
new stack once the previous one exceeds capacity.

.push() and .pop() should behave identically to a single stack

Follow up: implement a function .popAt()(int index) which performs
a pop operation on a specific sub-stack.

"""


class SetOfStacks:
    def __init__(self, stack_capacity: int):
        self.stacks = [[]]
        self.stack_capacity = stack_capacity

    @property
    def num_stacks(self) -> int:
        return len(self.stacks)

    @property
    def top_stack(self):
        return self.stacks[-1]

    def push(self, element: int):
        if len(self.top_stack) < self.stack_capacity:
            self.top_stack.append(element)
        else:
            new_stack = [element]
            self.stacks.append(new_stack)

    def pop(self) -> int:
        element = self.top_stack.pop()
        if len(self.top_stack) == 0 and self.num_stacks > 1:
            self.stacks.pop()
        return element

    def pop_at(self, stack_idx: int) -> int:
        if stack_idx > self.num_stacks - 1:
            raise Exception("index exceeds bounds")

        stack = self.stacks[stack_idx]
        element = stack.pop()
        if len(stack) == 0 and self.num_stacks > 1:
            self.stacks.pop(stack_idx)
        return element


if __name__ == "__main__":
    set_of_stacks = SetOfStacks(3)
    set_of_stacks.push(1)
    set_of_stacks.push(1)
    set_of_stacks.push(1)
    set_of_stacks.push(2)
    set_of_stacks.push(2)
    set_of_stacks.push(2)
    set_of_stacks.push(3)
    set_of_stacks.push(3)

    print("num_stacks =>", set_of_stacks.num_stacks)
    print("stacks =>", set_of_stacks.stacks)
    print("top_stack =>", set_of_stacks.top_stack)
    print()

    el = set_of_stacks.pop()
    print(el)
    el = set_of_stacks.pop()
    print(el)
    el = set_of_stacks.pop()
    print(el)

    print("num_stacks =>", set_of_stacks.num_stacks)
    print("stacks =>", set_of_stacks.stacks)
    print("top_stack =>", set_of_stacks.top_stack)

    set_of_stacks.push(4)
    set_of_stacks.push(4)
    set_of_stacks.push(4)
    set_of_stacks.push(5)
    set_of_stacks.push(5)

    print()
    print("num_stacks =>", set_of_stacks.num_stacks)
    print("stacks =>", set_of_stacks.stacks)
    print("top_stack =>", set_of_stacks.top_stack)
    print()

    el = set_of_stacks.pop_at(3)
    print(el)
    el = set_of_stacks.pop_at(1)
    el = set_of_stacks.pop_at(1)
    el = set_of_stacks.pop_at(1)
    print(el)
    el = set_of_stacks.pop_at(0)
    print(el)

    print("num_stacks =>", set_of_stacks.num_stacks)
    print("stacks =>", set_of_stacks.stacks)
    print("top_stack =>", set_of_stacks.top_stack)
