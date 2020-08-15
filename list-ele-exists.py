

def find_num(list_ele,ele_to_find):
    for i in list_ele:
        if i == ele_to_find:
            print("Element exists")
            return 0
    print("Element does not exists")
    
list_ele = [10, 45, 3, 88, 90, 123]
ele_to_find = 90
find_num(list_ele,ele_to_find)