def reversed_list(lst):
    return [ele for ele in reversed(lst)]

def listdotreverse(lst):
    lst.reverse()
    return lst

def manual_reversal(lst):
    new_lst = []
    ln = len(lst)
    for i in range (ln-1, -1, -1):
       # print(lst[i])
        new_lst.append(lst[i])
    return new_lst

def reverse_slicing(lst):
    new_list = lst[::-1]
    return new_list

lst = [10,11,12,13,14,15]
#print(reversed_list(lst))
#print(listdotreverse(lst))
#print(manual_reversal(lst))
print(reverse_slicing(lst))