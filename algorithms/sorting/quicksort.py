from algorithms.sorting.utils import check_sorting_algo


def quicksort(nums: list[float]) -> list[float]:
    """Quicksort

    Quicksort is an efficient in-place sorting algorithm, which
    usually performs about two to three times faster than mergesort
    and heapsort when implemented well.
    Quicksort is a comparison sort, meaning that it can sort items
    of any type for which a less-than relation is defined. In
    efficient implementations, it is usually not a stable sort.

    Quicksort, on average, makes O(n.log(n)) comparisons to sort
    n items. In the worst-case, it makes O(n2) comparisons, though
    this behavior is very rare.


    Quicksort is a Divide and Conquer algorithm. Like all
    divide-and-conquer algorithms, it first divides a large array
    into two smaller subarrays and then recursively sorts the
    subarrays. Basically, three steps are involved in the whole
    process:

    - Pivot selection: Pick an element, called a pivot, from the
        array (usually the leftmost or the rightmost element of
        the partition).
    - Partitioning: Reorder the array such that all elements with
        values less than the pivot come before the pivot. In contrast,
        all elements with values greater than the pivot come after it.
        The equal values can go either way. After this partitioning,
        the pivot is in its final position.
    - Recur: Recursively apply the above steps to the subarray of
        elements with smaller values than the pivot and separately to
        the subarray of elements with greater values than the pivot.

    Time: O(n.log(n)) average, worst O(n^2)
    Space: O(n) for the call stack
    """
    quicksort_resursive(nums, 0, len(nums) - 1)
    return nums


def swap(nums: list[float], i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums: list[float], start, end):
    # Pick the rightmost element as a pivot from the list
    pivot = nums[end]

    # elements less than the pivot will be pushed to the left of `pivot_idx`
    # elements more than the pivot will be pushed to the right of `pivot_idx`
    pivot_idx = start

    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if nums[i] <= pivot:
            swap(nums, i, pivot_idx)
            pivot_idx += 1

    # swap `pivot_idx` with pivot
    swap(nums, end, pivot_idx)

    return pivot_idx


def quicksort_resursive(nums: list[float], start: int, end: int):
    # base condition
    if end <= start:
        return

    # rearrange elements across pivot
    pivot_idx = partition(nums, start, end)

    # recur on sublist containing elements less than the pivot
    quicksort_resursive(nums, start, pivot_idx - 1)

    # recur on sublist containing elements more than the pivot
    quicksort_resursive(nums, pivot_idx + 1, end)


if __name__ == "__main__":
    check_sorting_algo(quicksort)
