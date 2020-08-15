def minele(lst): 
    return min(lst)

def minele_2(lst):
    min = lst[0]
    for ele in lst:
        if ele < min:
            min = ele
    return min

lst = []
count = int(input("Enter no of elemnts for list: "))
for i in range(1, count+1):
    ele = int(input("Enter elements: "))
    lst.append(ele)
print("Smallest element is:", minele(lst))
print("Smallest element using method 2 is ",minele_2(lst))

