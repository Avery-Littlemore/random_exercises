# In this problem, you're presented with a nested array, matrix, which has two key characteristics:

# Each subarray in the matrix is sorted in ascending order.
# The first element of each subarray is larger than the final element of the preceding subarray.

# Your task is to determine whether a given integer, target, exists within this nested array.
# The time complexity of your solution should be O(log(M*N)).

# M == rows
# N == columns

def find_in_nested_array(matrix, target):
    outer_left = 0
    outer_right = len(matrix) - 1

    while outer_left <= outer_right:
        outer_mid = (outer_left + outer_right) // 2
        
        current_subarray = matrix[outer_mid]

        left = 0
        right = len(current_subarray) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == current_subarray[mid]:
                return True
            elif target > current_subarray[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if left > 0:
            outer_left = outer_mid + 1
        else:
            outer_right = outer_mid - 1

    return False


print(find_in_nested_array([[4, 8, 12], [16, 20, 24], [28, 32, 36]], 20) == True)
print(find_in_nested_array([[3, 6, 9], [12, 15, 18], [21, 24, 27]], 27) == True)
print(find_in_nested_array([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 19) == False)
print(find_in_nested_array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 10) == True)
print(find_in_nested_array([[15, 25, 35], [45, 55, 65], [75, 85, 95]], 5) == False)