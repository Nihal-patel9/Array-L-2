def minDifference(nums, k):
    nums.sort()
    n = len(nums)
    min_score = float('inf')

    for i in range(k + 1):
        min_score = min(min_score, nums[n - k + i - 1] - nums[i])

    return min_score


nums = [1]
k = 0
min_score = minDifference(nums, k)
print(min_score)  # Output: 0
