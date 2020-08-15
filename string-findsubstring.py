import re

def check(str, sub_str):
    if (str.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")

def using_reg(str,sub_str):
    if re.search(sub_str,str):
        print("YES")
    else:
        print("NO")

def manual(str,sub_str):
    list_p = str.split(' ')
    for i in range (len(list_p)):

        if (sub_str == list_p[i]):
            return 1
       
str = "this is test pranav"
sub_str = "pran"
check(str, sub_str)
#using_reg(str,sub_str)
if (manual(str,sub_str)):
    print("YES")
else:
    print("NO")