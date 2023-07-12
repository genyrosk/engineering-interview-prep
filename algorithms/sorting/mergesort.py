from algorithms.sorting.utils import check_sorting_algo


def mergesort(nums: list[float]) -> list[float]:
    """Mergesort

    Mergesort works as a Divide and Conquer algorithm.
    Like all divide-and-conquer algorithms, merge sort divides a
    large array into two smaller subarrays and then recursively
    sorts the subarrays.

    The process has 2 steps:
    - Divide the unsorted array into n subarrays, each of size 1
        (an array of size 1 is considered sorted).
    - Repeatedly merge subarrays to produce new sorted subarrays
        until only 1 subarray is left, which would be our sorted array.

    Time:  O(n.log(n)) average, worst O(n^2)
    Space: O(n) for the call stack
    """
    aux = nums.copy()
    mergesort_resursive(nums, aux, 0, len(nums) - 1)
    return nums


def mergesort_resursive(nums: list[float], aux: list[float], low: int, high: int):
    if high <= low:
        return

    # midpoint
    mid = low + ((high - low) >> 1)

    mergesort_resursive(nums, aux, low, mid)
    mergesort_resursive(nums, aux, mid + 1, high)

    merge(nums, aux, low, mid, high)


def merge(nums: list[float], aux: list[float], low: int, mid: int, high: int):
    k = low  # total array
    i = low  # first sub-array from [low : mid]
    j = mid + 1  # second subarray [mid+1 : high]

    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            aux[k] = nums[i]
            i += 1
            k += 1
        else:
            aux[k] = nums[j]
            j += 1
            k += 1

    while i <= mid:
        aux[k] = nums[i]
        i += 1
        k += 1

    # No need to copy the second half (since the remaining items
    # are already in their correct position in the auxiliary array)

    # copy back from the auxilary array onto the original
    for i in range(low, high + 1):
        nums[i] = aux[i]


if __name__ == "__main__":
    check_sorting_algo(mergesort)
