def sum_dict(dict_a):
    sum = 0
    for i in dict_a:
        sum = sum + dict_a[i]
    return sum

def sum_dict2(dict_a):
    sum_dict = 0
    for i in dict_a.values():
        sum_dict = sum_dict + i
    return sum_dict


dict_a = {'a': 100,'b': 200,'c':300}
print(sum_dict(dict_a))
print(sum_dict2(dict_a))