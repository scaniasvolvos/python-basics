def retEvenStr(str):
    str = str.split(' ')
    #print(temp)
    for i in str:
        if (len(i) % 2 == 0):
            print(i, end=' ')


str = "My name is Pranav rrr ppppp pppp"
retEvenStr(str)
