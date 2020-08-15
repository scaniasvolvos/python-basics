def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr,n)
def leftRotateByOne(arr, n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def printArray(arr,l):
    for i in range(l):
        print("%d"% arr[i],end=" ")

arr = [1,2,3,4,5,6,7]
l = len(arr)
print(l)
leftRotate(arr, 2, l)
#printArray(arr, l)
print(arr)