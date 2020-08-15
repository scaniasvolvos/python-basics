def dictionary():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[4] = 44
    key_value[3] = 90
    
    print("Task 1:-\n")
    print("Keys are")

#    for i in (key_value.keys()):
#        print((i,key_value[i]), end=' ')

    for i in sorted(key_value.keys()):
        print((i, key_value[i]), end=' ')

def main():
    dictionary()

if __name__ == "__main__":
    main()