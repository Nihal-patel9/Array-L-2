def findLHS(nums):
    freq_dict = {}
    max_length = 0

    # Count the frequency of each number

    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Iterate over the dictionary keys

    for num in freq_dict.keys():
        if num + 1 in freq_dict:
            current_length = freq_dict[num] + freq_dict[num + 1]
            max_length = max(max_length, current_length)

    return max_length


nums = [1, 3, 2, 2, 5, 2, 3, 7]
max_subseq_length = findLHS(nums)
print(max_subseq_length)  # Output: 5
