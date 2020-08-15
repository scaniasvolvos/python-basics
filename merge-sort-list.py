
# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr1,arr2): 
    arr = []
    for i,j in zip(arr1,arr2):
        arr.append(i)
        arr.append(j)
    #print(arr)

    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
        
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            print(type(arr[j]))
            if (type(arr[j]) == "<class 'int'>"):
                print("This is an integer")
            
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
        
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
  
# Driver code to test above 
arr1 = [64, 34, 25] 
arr2 = [12, 22, 11] 
  
bubbleSort(arr1,arr2) 
