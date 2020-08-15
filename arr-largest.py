def largest(arr, n):
    max  = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10, 20, 65, 500]
n = len(arr)
max = largest(arr, n)
print("Largest element is", max)