test_tup = (7,8,9,1,10,7)

print("Original tuple is: " + str(test_tup))

res = list(test_tup)
print(type(res))

sum = 0
for i in res:
    sum = sum + i
print (sum)


