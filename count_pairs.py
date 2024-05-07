# In this problem, you are provided with an ascending order array of integers, nums. 
# Your task is to count the number of pairs in this array whose sum is greater than a given target value, target.

# Constraints:
# The array nums is sorted in ascending order.
# No duplicate pairs should be counted. For instance, if nums contains [1, 2] and target is 2, 
# then (1, 2) is a valid pair since 1 + 2 > 2. You shouldn't include (2, 1)

def count_pairs(nums, target):
    start = 0
    end = len(nums) - 1
    total = 0

    while start < len(nums) - 1:
        if nums[start] + nums[end] > target:
            total += 1
            end -= 1
        else:
            start += 1
            end = len(nums) - 1

        if start == end:
            start += 1
            end = len(nums) - 1

    return total


print(count_pairs([1, 2, 3, 4, 5], 6) == 4)
# Pairs: (2, 5), (3, 4), (3, 5), (4, 5)

print(count_pairs([1, 2, 3, 4, 5], 8) == 1)
# Pair: (4, 5)

print(count_pairs([1, 3, 5, 7], 6) == 4)
# Pairs: (1, 7), (3, 5), (3, 7), (5, 7)

print(count_pairs([1, 2, 3, 4], 5) == 2)
# Pairs: (2, 4), (3, 4)

print(count_pairs([1, 2, 3, 4, 5], 10) == 0)
# No pairs