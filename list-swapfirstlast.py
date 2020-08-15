def swaplist(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


newList = [10, 34, 65, 78]
print(swaplist(newList))