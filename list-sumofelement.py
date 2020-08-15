def iterate_and_add(lst):
    #ln = len(lst)
    total = 0
    for ele in lst:
        total = total + ele
    return total

def built_in_sum(lst):
    total = sum(lst)
    return total

lst = [10,11,12,13,14,15]
print("Sum of elements in list ",lst," is ",iterate_and_add(lst))
#print(built_in_sum(lst))