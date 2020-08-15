dict1 = {'Name': 'Pranav', 'Age': 23}
dict2 = {'Id': 12345}
sequ = ('Name', 'Age', 'Id')

dict1.update(dict2)
print(str(dict1))

# Initalize a seq and populate the def values in dict using fromkeys()
dict_sequ = dict.fromkeys(sequ,5)
print(str(dict_sequ))

# Use in operator to check keys of dict
dict = { 'Name' : 'Nandini', 'Age' : 19 }
if 'Name' in dict:
    print("Key present and its value is {}".format(dict.get('Name')))
else: print("Key not present")


#Use of get method
print(dict.popitem())
print("The value associated with key Age is : ", dict.get('Age', 'Not Present'))

#If key is not present, insert it with a def valu using setdefault()
print("The value associated with key ID is : ", dict.setdefault('ID', 'No ID'))
print(str(dict))