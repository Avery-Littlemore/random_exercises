# Given an array nums, sorted in ascending order (where elements are equal to or increase as you move through the array), 
# determine if a specified number, target, appears more than three times in the array. The function should return True if target is found at least four times, and False otherwise.

def isTargetFrequent(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        total = 0
        
        if nums[mid] == target:
            iterator = 0
            while mid + iterator < len(nums) and nums[mid + iterator] == target:
                total += 1
                iterator += 1
            
            iterator = 1
            while mid - iterator >= 0 and nums[mid - iterator] == target:
                total += 1
                iterator += 1

            if total >= 4:
                return True
            else:
                return False
                
        elif nums[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
        


    return False

print(isTargetFrequent([1, 2, 3, 3, 3, 3, 4], 3) == True)
print(isTargetFrequent([1, 1, 1, 1, 2, 3, 4], 1) == True)
print(isTargetFrequent([1, 2, 3, 4, 5], 2) == False )
print(isTargetFrequent([1, 1, 3, 4, 5], 2) == False )
print(isTargetFrequent([2, 2, 2, 3, 3, 3, 4], 3) == False)
print(isTargetFrequent([4, 4, 4, 4, 4, 4, 4], 4) == True)