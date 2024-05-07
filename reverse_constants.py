# Given a string str, reverse only all the consonants in the string and return it. 
# Consonants are all alphabetic characters except for the vowels 'a', 'e', 'i', 'o', 
# and 'u', which can appear in both lower and upper cases. The consonants can appear more than once in the string.

def reverse_constants(str):
    left = 0
    right = len(str) - 1
    vowels = 'AEIOUaeiou'
    str_array = list(str)
    while left <= right:
        if str_array[left] in vowels:
            left += 1
            continue
        elif str_array[right] in vowels:
            right -= 1
            continue
        else:
            [str_array[left], str_array[right]] = [str_array[right], str_array[left]]
            left += 1
            right -= 1
    return ''.join(str_array)

print(reverse_constants("") == "")
print(reverse_constants("s") == "s")
print(reverse_constants("hello") == "lelho")
print(reverse_constants("leetcode") == "deectole")
print(reverse_constants("example") == "elapmxe")
print(reverse_constants("Consonants") == "sotnonasnC")

# // All test cases should log true