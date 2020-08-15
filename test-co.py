def count_occr():
    
    count  =  0
    
    for i in lis:
        if num == i:
            count += 1
    return count

lis = [2,1,3,5,4,3,8]
num = 3
print("The occurence of num ", num, " is ",count_occr())