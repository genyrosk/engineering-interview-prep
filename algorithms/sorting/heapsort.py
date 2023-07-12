from algorithms.sorting.utils import check_sorting_algo


def left_child(i: int) -> int:
    return 2 * i + 1


def right_child(i: int) -> int:
    return 2 * i + 2


def swap(nums: list[float], i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def heapify(nums: list[float], i: int, size: int):
    """Similar to build_max_heap, but assumes that part
    of the array is already sorted.

    Recursive heapify-down algorithm. The node at index `i` and
    its two direct children violates the heap property
    """

    left = left_child(i)
    right = right_child(i)

    largest = i

    if left < size and nums[left] > nums[i]:
        largest = left

    if right < size and nums[right] > nums[largest]:
        largest = right

    # swap with a child having greater value and
    # call heapify-down on the child
    if largest != i:
        swap(nums, i, largest)
        heapify(nums, largest, size)


def pop(nums: list[float], size: int):
    """
    Function to remove an element with the highest priority (present at the root)
    """
    # if the heap has no elements
    if size <= 0:
        return -1

    top = nums[0]

    # replace the root of the heap with the last element
    # of the list
    nums[0] = nums[size - 1]

    # call heapify-down on the root node
    heapify(nums, 0, size - 1)

    return top


def heapsort(nums: list[float]) -> list[float]:
    """Heasort

    Heapsort is an in-place, comparison-based sorting algorithm
    and can be thought of as an improved selection sort as it
    divides the input into a sorted and an unsorted region. It
    iteratively shrinks the unsorted region by extracting the
    largest/smallest element and moving that to the sorted region.
    The improvement consists of using a heap data structure rather
    than a linear-time search to find the maximum.

    Heapsort does not produce a stable sort, which means that the
    implementation does not preserve the input order of equal
    elements in the sorted output. It is generally slower than
    other O(n.log(n)) sorting algorithms like quicksort, mergesort.

    The heapsort algorithm can be divided into two parts:

    - 1. In the first step, a max-heap is built out of the input data.
        We can do this in O(n) time.
    - 2. Remove the largest item
    - 3. Place the item in sorted partition. In thisstep, a sorted array is created by repeatedly
        removing the largest/smallest element from the heap (the root
        of the heap) and inserting it into the array. The heap is
        updated (heapify-down is called on the root node) after each
        removal to maintain the heap property. Once all elements have
        been removed from the heap, we get a sorted array. This is
        done in O(n.log(n)) time since we need to pop n elements,
        where each removal involves a constant amount of work and a
        single heapify operation takes O(log(n)) time.

    Time: O(n.log(n)) average
    Space: O(n)
    """
    # build a priority queue and initialize it by the given list
    n = len(nums)

    # Build-heap: Call heapify starting from the last internal
    # node all the way up to the root node
    i = (n - 2) // 2
    while i >= 0:
        heapify(nums, i, n)
        i -= 1

    # repeatedly pop from the heap till it becomes empty
    while n:
        nums[n - 1] = pop(nums, n)
        n = n - 1

    return nums


if __name__ == "__main__":
    check_sorting_algo(heapsort)
