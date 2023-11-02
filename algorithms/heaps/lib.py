from heapq import heapify, heappop, heappush


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 2, 4, 2, 7, 6, 9, 7]
    heapify(nums)
    print(nums)
    heappush(nums, 10)
    print(nums)
    _min = heappop(nums)
    print("min", _min)
    print(nums)
