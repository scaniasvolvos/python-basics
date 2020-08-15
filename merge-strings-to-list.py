str1 ="'Geeks', 'for', 'Geeks'"
str2 ="'paras.j', 'jain.l'"
str3 ="'india'"

list = []
result = []

list.append(str1.split(','))
list.append(str2.split(','))
list.append(str3.split(','))
#print (list)

for i in list:
    for j in i:
        result.append(j)

print (result)
