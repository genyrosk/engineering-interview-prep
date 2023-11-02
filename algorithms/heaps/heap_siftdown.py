from heapq import heapify, heappush


def swap(nums: [float], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent_cell(i):
    return i // 2


def sift_down(nums: [float], i: int, size: int):
    left = left_child(i)
    right = right_child(i)
    smallest = i

    if left < size and nums[left] < nums[smallest]:
        smallest = left
    if right < size and nums[right] < nums[smallest]:
        smallest = right

    if smallest != i:
        swap(nums, i, smallest)
        sift_down(nums, smallest)


def sift_up(nums: [float], i: int):
    if i == 0:
        return

    parent = parent_cell(i)

    if nums[parent] > nums[i]:
        swap(nums, i, parent)
        sift_up(nums, parent)


if __name__ == "__main__":
    nums = [5, 2, 4, 3, 8, 5, 8, 9, 5]
    heap = []

    for num in nums:
        heap.append(num)
        sift_up(heap, len(heap) - 1)
        print(heap)

    print("my heap:", heap)

    heapify(heap)
    print("heapify:", heap)

    correct_heap = []
    for num in nums:
        heappush(correct_heap, num)
    print("correct heap:", correct_heap)
