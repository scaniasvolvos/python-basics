def findLen(str):
    counter = 0
    for _ in str:
        counter += 1
    return counter


str = "teststr"
print(len(str))
print(findLen(str))
