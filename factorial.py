def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n-1)


n = 6
print("Factorial of {} is {}".format(n,factorial(n)))