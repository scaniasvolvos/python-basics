lis = [1,2,3]
lis_2 = [4,5,6]

# Concatenating using +
lis_res = lis + lis_2
print("List after concatenation : ", end="")
for i in range(len(lis_res)):
    print(lis_res[i],end=" ")

print("\r")

# Combining using *
lis_mul = lis * 3
print("List after combining : ", end="")
for i in range(len(lis_mul)):
    print(lis_mul[i],end=" ")

print("\r")

#Use if index() to print occurance of an element after certain index
print("The first oocurence of 3 after 3rd position is : ",end="")
print(lis_mul.index(3,3,9))

print("\r")

#Use count() to count the number of occurences in a list
print("3 has occured",lis_mul.count(3),"times")

#Use del <listname> [start:end] to delete range of elements
lis = [2,1,3,5,4,3,8]
del lis[2:5]
print("Lists are deleting the elements: ",end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

print("\r")

# Pop element using pop() from a certain position
lis.pop(2)


print("List after poppping elemts are :",end="")
for i in range(0,len(lis)):
    print(lis[i], end=" ") 
'''
def count_occr():
    count  =  0    
    for i in lis:
        if num == i:
            count += 1
    return count
lis = [2,1,3,5,4,3,8]
num = 3
print(count_occr())
'''
