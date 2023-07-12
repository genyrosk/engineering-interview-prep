import math

"""
TODO: implement a heap with insertions and deletions,
emulating a real-life system such as a priority queue
or scheduler.
"""


class MaxHeap:
    def __init__(self, max_size: int, data: list[float] = None):
        self.size = 0
        self.max_size = max_size
        self.heap = [0] * max_size

    def left_child(self, idx: int) -> int:
        return 2 * idx + 1

    def right_child(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return idx // 2

    def is_leaf(self, idx: int) -> bool:
        return idx >= self.size // 2 and idx <= self.size

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def max_heapify(self, idx: int):
        if self.is_leaf(idx):
            return

        node = self.heap[idx]
        left_idx = self.left_child(idx)
        left = self.heap[left_idx]
        right_idx = self.right_child(idx)

        if right_idx >= self.size:
            if node > left:
                self.swap(idx, left_idx)
                self.max_heapify(left_idx)
            return

        print(idx, right_idx)
        right = self.heap[right_idx]

        satisfies_heap_property = node > left and node > right
        if satisfies_heap_property:
            return

        if left > right:
            self.swap(idx, left_idx)
            self.max_heapify(left_idx)
        else:
            self.swap(idx, right_idx)
            self.max_heapify(right_idx)

    def insert(self, element: float):
        if self.size >= self.max_size:
            return

        self.heap[self.size] = element
        idx = self.size

        while self.heap[idx] > self.heap[self.parent(idx)]:
            self.swap(idx, self.parent(idx))
            idx = self.parent(idx)

        self.size += 1

    def __repr__(self) -> str:
        string = ""
        print(self.heap)

        n_levels = math.ceil(math.log(self.size, 2))
        base_pad = 4

        def is_power_of_two(n: int):
            return math.ceil(math.log(n, 2)) == math.floor(math.log(n, 2))

        for i in range(0, self.size):
            level = math.trunc(math.log(i + 1, 2))
            to_pad = n_levels - level - 1
            side_pad = " " * ((to_pad * base_pad))
            if i == 0 or is_power_of_two(i + 1):
                string += "\n"
            string += f"{self.heap[i]: <3} "
            string += side_pad
        string += "\n"
        return string

    def pop_max(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return popped


# def build_max_heap(nums: list[float]):
#     """
#     A Max-Heap is a complete binary tree in which the
#     value in each internal node is greater than or
#     equal to the values in the children of that node.

#     Mapping the elements of a heap into an array is
#     trivial: if a node is stored a index k, then its
#     left child is stored at index 2k + 1 and its right
#     child at index 2k + 2.
#     """

#     pass


if __name__ == "__main__":
    print("The maxHeap is ")

    maxHeap = MaxHeap(55)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.insert(9)

    print(maxHeap)

    print("The Max val is " + str(maxHeap.pop_max()))
