with open ("file_write.txt","w") as file:
    for i in range (1,11):
        file.writelines(["This is line {}\n".format(i)])
    

file = open("file_write.txt", "r" )
for line in (file.readlines() [7:10]):
    print(line, end = '')
