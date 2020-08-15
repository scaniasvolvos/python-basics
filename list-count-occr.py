def count_occr(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count

def countX(lst, num):
    return lst.count(num)

lst = [12, 45, 76, 45, 90, 90, 90]
num = 90
print("The element", num," occurs",count_occr(lst, num),"times")
print("The element",num," occurs",countX(lst, num), "times")