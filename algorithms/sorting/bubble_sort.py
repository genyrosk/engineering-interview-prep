from algorithms.sorting.utils import check_sorting_algo


def bubble_sort(nums: list[float]) -> list[float]:
    """Bubble sort

    Traverse left to right and compare adjacent elements.
    The higher one is placed to the right side.
    If it's smaller, stop and start again from the start.
    This way, the large values are "bubbled up" to the end of the array.

    Time: O(n^2), worst: O(n^2), best: O(n)
    Space: O(1) or O(2)
    """
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                aux = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = aux
                swapped = True
        # array is sorted: early break
        if not swapped:
            break
    return nums


if __name__ == "__main__":
    check_sorting_algo(bubble_sort)
