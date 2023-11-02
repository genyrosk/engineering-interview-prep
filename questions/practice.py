def threeSumZero(nums: [int]):
    if len(nums) < 3:
        return None

    positives = [num for num in nums if num > 0]
    zeros = [num for num in nums if num == 0]
    negatives = [num for num in nums if num < 0]

    if len(zeros) >= 3:
        return [0, 0, 0]
    if len(zeros) > 0:
        positives.append(0)
    if len(positives) + len(negatives) < 3:
        return None
    if len(positives) == 0 or len(negatives == 0):
        return None

    positives_set = set(positives)  # O(n)
    negatives_set = set(negatives)  # O(n)

    # pick 2 numbers in positives => negative sum that I can find in negatives
    # and if not, try the same thing in reverse

    for i in range(len(positives) - 1):  # O(n)
        for j in range(i + 1, len(positives)):  # O(n)
            a = positives[i]
            b = positives[j]

            _sum = a + b

            if -_sum in negatives_set:  # O(1)
                return (a, b, -_sum)

    for i in range(len(negatives) - 1):  # O(n)
        for j in range(i + 1, len(negatives)):  # O(n)
            a = negatives[i]
            b = negatives[j]

            _sum = a + b

            if -_sum in positives_set:  # O(1)
                return (a, b, -_sum)

    return None


# Time complexity: O(n^2)
# Space complexity: O(n)


nums1 = [3, 5, 8, 10, -9, -11]  # => [3,8,-11]
nums2 = [3, 5, 4, 9, -16]  # => None

nums3 = [3, 1, -10, -1, -3]  # =>
nums4 = [0, 0, 0, 1]
nums5 = []
nums6 = [1, 2, 3]
nums7 = [-1, -2, -3]
nums8 = [0, 0, 1]

sol = threeSumZero(nums1)
print(sol)
sol = threeSumZero(nums2)
print(sol)
sol = threeSumZero(nums3)
print(sol)
sol = threeSumZero(nums4)
print(sol)
sol = threeSumZero(nums5)
print(sol)
sol = threeSumZero(nums6)
print(sol)
sol = threeSumZero(nums8)
print(sol)
