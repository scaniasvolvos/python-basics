
def FindMaxLength(lst):
    maxList = 0
    list = []
    for x in lst:
        #print (len(x))
        if (len(x) > maxList):
            maxList = len(x)
            list = x

    return list,maxList



lst = [['A'], ['A', 'B'], ['A', 'B', 'C']] 
print(FindMaxLength(lst)) 