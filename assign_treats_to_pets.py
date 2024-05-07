# Imagine you're a pet owner wanting to give treats to your pets. Each pet has a specific appetite level represented by 
# an array appetite[i], which is the minimum size of a treat the pet will be happy with. Each treat has a size represented 
# by an array treats[j]. A pet will be satisfied if the size of the treat treats[j] is greater than or equal to its appetite 
# level appetite[i]. Your goal is to maximize the number of satisfied pets and output the number of satisfied pets in the end.

def assign_treats(appetite, treats):
    appetite.sort()
    treats.sort()

    # a_anchor = 0
    a_runner = 0
    # t_anchor = 0
    t_runner = 0
    total = 0

    while a_runner < len(appetite) and t_runner < len(treats):
        if appetite[a_runner] <= treats[t_runner]:
            total += 1
            a_runner += 1
            t_runner += 1
        else:
            t_runner += 1

    return total

print(assign_treats([3, 4, 2], [1, 2, 3]) == 2)
print(assign_treats([1, 5], [5, 5, 6]) == 2)
print(assign_treats([1, 2, 3], [3]) == 1)
print(assign_treats([2], [1, 2, 1, 1]) == 1)
print(assign_treats([4, 3, 1], [2, 1, 3]) == 2)
print(assign_treats([1,2,3], [1,2,3]) == 3)
print(assign_treats([4, 5, 6], [1,2,3]) == 0)