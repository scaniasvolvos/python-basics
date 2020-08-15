def second_largest(lst):
    largest = max(lst[0],lst[1])
    sec_largest = min(lst[0],lst[1])
    for i in range(2,len(lst)):
        if lst[i] > largest:
            sec_largest = largest
            largest = lst[i]
        elif lst[i] > sec_largest and largest != lst[i]:
            sec_largest = lst[i]
    return sec_largest


lst = [10, 20, 15, 3]
#lst.sort()
#print("Second largest element is ",lst[-2])
print("Second largest element is ",second_largest(lst))