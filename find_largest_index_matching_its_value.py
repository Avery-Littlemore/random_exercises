# Given an array nums of distinct integers sorted in ascending order, your task is to find the largest index j 
# such that nums[j] is equal to j. If no such index exists, return -1.

def findLargestIndex(array):
    left = 0
    right = len(array) - 1
    highest = -1
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == mid:
            highest = mid
            left = mid + 1
        elif array[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    
    return highest

print(findLargestIndex([-1, 0, 2, 3]) ==  3)
print(findLargestIndex([0, 1, 2, 3, 4]) ==  4)
print(findLargestIndex([-5, 0, 3, 4, 7, 9]) == -1)
print(findLargestIndex([-2, 0, 1, 3, 3, 5]) ==  5)
print(findLargestIndex([0]) ==  0)