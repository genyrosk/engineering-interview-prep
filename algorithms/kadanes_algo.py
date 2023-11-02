"""
Kadane's algorithm solves the max-subarray problem in learn time O(n).

The max subarray problem is about finding a contiguous subarray with the
maximum sum possible in an array composed of positive and negative numbers.
"""


def kadane(nums: [float]):
    """Find the largest sum of any contiguous subarray."""
    current_sum = 0
    max_sum = float("-inf")

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = kadane(nums)
    print("max_sum:", max_sum)
