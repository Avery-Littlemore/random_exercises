# In this provided, you're given an array of numbers nums, and a specific integer k. 
# Your objective is to compute the average value of each contiguous subarray of length k within the given array.

# Requirements:
# The input will be an array of numbers and an integer k.
# You need to find the average of every contiguous subarray of size k in the array.
# The output should be an array containing these averages.

def find_averages(nums, k):
    start = 0
    end = start + k - 1
    result = []
    sum = 0

    while end < len(nums):
        for i in range(start, end + 1):
            sum += nums[i]
        result.append(sum / k)
        sum = 0
        start += 1
        end += 1

    return result

print(find_averages([1, 2, 3, 4, 5, 6], 3))  # [ 2, 3, 4, 5 ]
print(find_averages([1, 2, 3, 4, 5], 2))     # [1.5, 2.5, 3.5, 4.5]
print(find_averages([10, 20, 30, 40, 50], 4))  # [ 25, 35 ]
print(find_averages([5, 5, 5, 5, 5], 1))       # [ 5, 5, 5, 5, 5 ]
print(find_averages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))  # [2.2, 2.8, 2.4, 3.6, 2.8]