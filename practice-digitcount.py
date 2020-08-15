n = int(input("Enter number: "))
count = 0

if n == 0:
    count = 1

while (n>0):
    count+=1
    n=n//10
print("Number of digits in number is/are: ",count)