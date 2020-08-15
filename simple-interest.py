def simple_interest(p, t, r):
    return (float(p * t * r)/100)


#if __name__ == '__main__':
principal = int(input("P = "))
rate = float(input("R = "))
time = int(input("T = "))
si = simple_interest(principal, time, rate)
print ("The simple interest is :", si)