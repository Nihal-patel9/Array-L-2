def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    total_sum = 0
    for i in range(0, len(nums), 2):
        total_sum += nums[i]
    return total_sum


nums = [1, 4, 3, 2]
max_sum = arrayPairSum(nums)
print(max_sum)  # Output: 4
