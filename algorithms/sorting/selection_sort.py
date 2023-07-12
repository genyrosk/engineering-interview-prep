from algorithms.sorting.utils import check_sorting_algo


def selection_sort(nums: list[float]) -> list[float]:
    """Selection sort

    Divide the Array into 2 subsets - a sorted and unsorted subset. The algorithm
    finds the smallest (or largest) element in the unsorted subset and swaps it
    with the leftmost unsorted element and moving the subset boundary one element
    to the right.

    It outperforms Bubble Sort, but is usually worse than Insertion sort.
    The main advantage of Select Sort is that it does at most `n` swaps
    (memory write). Insertion sort on the other hand does O(n^2) writes.
    This can be critical if memory-write operation is significantly more
    expensive than memory-read ops, such as flash memory.

    Time: O(n^2) average, best and worst
    Space: O(1)
    """
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    check_sorting_algo(selection_sort)
