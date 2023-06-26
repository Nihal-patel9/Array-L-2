def maximumProduct(nums):
    nums.sort()  # Sort the array in ascending order

    # Case 1: All numbers are non-negative
    max_product = nums[-1] * nums[-2] * nums[-3]

    # Case 2: There are negative numbers
    if nums[0] < 0 and nums[1] < 0:
        max_product = max(max_product, nums[0] * nums[1] * nums[-1])

    return max_product


nums = [1, 2, 3]
max_prod = maximumProduct(nums)
print(max_prod)  # Output: 6
