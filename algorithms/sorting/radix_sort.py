def digit_count_sort(nums, exp):
    n = len(nums)
    counts = [0] * 10
    output = [0] * n

    # count digit occurences
    for num in nums:
        idx = num // exp % 10
        counts[idx] += 1

    # calcualte cumulative -> places the digit in the right place
    for i in range(1, 10):
        counts[i] += counts[i - 1]

    # build output array
    i = n - 1
    while i >= 0:
        idx = nums[i] // exp % 10
        count = counts[idx]
        output[count - 1] = nums[i]
        counts[idx] -= 1
        i -= 1

    # copy output back to original array
    for i in range(n):
        nums[i] = output[i]


def radix_sort(nums: [int]):
    _max = max(nums)

    exp = 1
    while _max / exp >= 1:
        digit_count_sort(nums, exp)
        exp *= 10

    return nums


if __name__ == "__main__":
    nums = [1, 23, 2, 42, 61, 28, 100]
    s = radix_sort(nums)
    print(s)
