# Write a function that checks whether a given positive integer num is the result of an integer multiplied by itself, 
# which is typically referred to as a square integer. The function should return True if num is a square integer, 
# otherwise false. The implementation should not rely on any square root computation provided by built-in Math library.

def isSquareInteger(num):
    highest = num
    lowest = 1

    while lowest <= highest:
        mid = (highest + lowest) // 2

        if mid * mid == num:
            return True
        elif mid * mid < num:
            lowest = mid + 1
        else:
            highest = mid - 1

    return False

print(isSquareInteger(1) == True)
print(isSquareInteger(4) == True)
print(isSquareInteger(16) == True)
print(isSquareInteger(14) == False)
print(isSquareInteger(25) == True)
print(isSquareInteger(26) == False)