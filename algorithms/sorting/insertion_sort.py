from algorithms.sorting.utils import check_sorting_algo


def insertion_sort(nums: list[float]) -> list[float]:
    """Insertion sort

    Insertion sort is a stable, in-place sorting algorithm that builds the
    final sorted array one item at a time. It is not the very best in terms of
    performance but more efficient traditionally than most other simple O(n2)
    algorithms such as selection sort or bubble sort.

    It is also a well known online algorithm since it can sort a list as
    it receives it. In all other algorithms, we need all elements to be
    provided to the sorting algorithm before applying it.
    With insertion sort, we can start we a partial set of elements and sort them.
    Then insert more elements and sort them.
    In the real world, data to be sorted is usually not static, rather dynamic.
    If even one additional element is inserted during the sorting process,
    other algorithms don't respond easily. But only insertion sort algorithm
    is not interrupted and can respond well with the additional element

    The idea is to divide the array into two subsets - sorted subset
    and unsorted subsets. For each iteration, insertion sort removes the next
    element from the unsorted subset, finds the location it belongs within
    the sorted subset and inserts it there.

    Time: O(n^2), worst: O(n^2) (if the list is reversed), best: O(n)
    Space: O(1) and O(n) in recursive implementation
    """
    for i in range(1, len(nums)):
        value = nums[i]

        j = i
        while j > 0 and value < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1

        nums[j] = value

    return nums


def insertion_sort_resursive_call(nums: list[float], i: int, length: int):
    """
    Time: O(n^2), worst: O(n^2) (if the list is reversed), best: O(n)
    Space: O(n)
    """
    value = nums[i]
    j = i
    while j > 0 and value < nums[j - 1]:
        nums[j] = nums[j - 1]
        j -= 1

    nums[j] = value
    if i + 1 <= length:
        return insertion_sort_resursive_call(nums, i + 1, length)

    return nums


def insertion_sort_resursive(nums: list[float]) -> list[float]:
    return insertion_sort_resursive_call(nums, 1, len(nums) - 1)


if __name__ == "__main__":
    check_sorting_algo(insertion_sort)
    check_sorting_algo(insertion_sort_resursive)
