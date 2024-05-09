# Given an array nums sorted in ascending order, determine the minimum between the count of positive integers and the count of negative integers.

# Please note that the number 0 is neither positive nor negative.

def minimum_count(array):
    if not array:
        return 0
    
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1
    
    pos_nums = len(array) - right - 1

    left = 0
    right = len(array) - right

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1
    
    neg_nums = left

    return min(neg_nums, pos_nums)

            


print(minimum_count([-4, -3, -2, -1, 3, 4]) == 2)
print(minimum_count([-3, 1, 2, 3, 4, 5]) == 1)
print(minimum_count([-5, -4, -3, -2, -1]) == 0)
print(minimum_count([1, 2, 3, 4, 5]) == 0)
print(minimum_count([-2, -1, 1, 2]) == 2)
print(minimum_count([-7, -5, -4, 1, 2, 6, 10]) == 3)
print(minimum_count([-3, -2, -1, 0, 5, 6]) == 2)
print(minimum_count([-1, 0, 1]) == 1)
print(minimum_count([]) == 0)