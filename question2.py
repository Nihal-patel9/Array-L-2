def maxCandies(candyType):
    different_candies = set(candyType)
    max_candies = len(different_candies)
    half_candies = len(candyType) // 2

    if max_candies <= half_candies:
        return max_candies
    else:
        return half_candies


candyType = [1, 1, 2, 2, 3, 3]
max_types = maxCandies(candyType)
print(max_types)  # Output: 3
