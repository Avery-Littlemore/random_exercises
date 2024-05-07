# You have an ordered array nums consisting of integers. Your task is to determine whether there are any two 
# distinct elements in the array where one element is exactly three times the value of the other element. The 
# time complexity of the solution should be O(N).

# Restrictions:

# You should not use built-in methods like filter, map, reduce, or find.
# Do not use the includes method for checking existence in the array.
# Avoid using indexOf or lastIndexOf.

def check_triple_match(nums):
    hash_table = {}

    for num in nums:
        hash_table[num] = True

        if num == 0:
            continue
        if hash_table.get(num * 3) or hash_table.get(num / 3):
            return True
    
    return False

print(check_triple_match([1, 3, 9, 28]) == True)
print(check_triple_match([1, 2, 4, 10, 11, 12]) == True)
print(check_triple_match([0, 5, 7, 55]) == False)
print(check_triple_match([4, 5, 7, 9, 13, 15, 17]) == True)
print(check_triple_match([2, 6, 13, 54]) == True)
print(check_triple_match([1, 5, 17, 51]) == True)
print(check_triple_match([1, 2, 4, 8]) == False)