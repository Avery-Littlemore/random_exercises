# Given an array of integers nums, sorted in ascending order (where elements are equal to or increase as you move through the array), 
# your task is to implement a function reduceToUnique. This function should modify the array in-place ensuring that it starts with a 
# sequence of unique elements each following their original order in the array. After these modifications, return the count of these 
# unique elements.

# The elements in the latter part of the array, after the unique ones, are not important. The key requirement is that the array should 
# remain the same object as the input and should be modified to reflect the changes.

def reduce_to_unique(array):
    anchor = 0
    pointer = 1
    while pointer < len(array):
        if array[anchor] == array[pointer]:
            pointer += 1
        else:
            array[anchor + 1] = array[pointer]
            anchor += 1
            pointer += 1
    
    return len(array[:anchor + 1])
            

def test_reduce_to_unique(array, expected_length):
    original_reference = array
    result_length = reduce_to_unique(array)
    is_same_object = original_reference == array
    is_length_correct = result_length == expected_length
    is_modified_correctly = all(array[i] > array[i - 1] for i in range(1, expected_length))

    return is_same_object and is_length_correct and is_modified_correctly

print(test_reduce_to_unique([3, 3, 5, 7, 7, 8], 4))
print(test_reduce_to_unique([1, 1, 2, 2, 2, 3, 4, 4, 5], 5))
print(test_reduce_to_unique([0], 1))
print(test_reduce_to_unique([-5, -3, -3, -1, 0, 0, 0, 1], 5))
print(test_reduce_to_unique([6, 6, 6, 6, 6, 6, 6], 1))
