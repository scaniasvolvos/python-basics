dic = {'Name' : 'Nandini', 'Age': 19}
dic_temp = {}
#dic_per = {'Name' : 'Nandini', 'Age': 22}
li = [1,2,3,4,5]
# Returns dict in str format
print("The elements of dict in string are : ", str(dic))
# Returns dict in list format)
print("The elements of dict in list are :", dic.items())
print("The size of dict is: ", len(dic))
print("The type of dic is: ", type(dic))
print("The type of li is: ", type(li))
dic_temp = dic.copy()
print("Copied dict: ",dic_temp.items())
dic.clear()
print("Items in dic are: ",dic.items())