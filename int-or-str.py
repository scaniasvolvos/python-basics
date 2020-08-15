list = [3,4,"scania","volvo",67]
new_list=[]
new_str=[]
for i in list:
    if isinstance(i,int):
        new_list.append(i)
    elif isinstance(i,str):
        new_str.append(i)
print(new_list)
print(new_str)