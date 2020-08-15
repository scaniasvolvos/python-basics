import os

path = 'C:/Users/prana/Documents'
dir_list = os.listdir(path)
print(dir_list)

with open (os.path.join(path,'test.txt'), 'w+') as fp:
    fp.write("New file created")
fp.close()
print(os.listdir(path))

with open (os.path.join(path,'test.txt'), 'r') as fp:
    print(fp.read())

#print(dir_list)



fp = open(os.path.join(path,'test.txt'), 'r')
print (fp.read(5))

file = open(os.path.join(path,'demo.txt'), 'w')
file.write("This is a demo file")
print(os.listdir(path))
file.close()
with open (os.path.join(path,'demo.txt'),'r') as fp:
    print(fp.read())
fp.close()
print("---------------------")
file_a = open(os.path.join(path,'demo.txt'),'a')
for i in range(10):
    file_a.write("\nThis is appended line {}".format(i))
file_a.close()
with open(os.path.join(path,'demo.txt'),'r') as fp:
    data  = fp.readlines()
    #print (data)
    for line in data:
        word = line.split()
        print (word)
print("---------------------------------------------------------------")
new_file = open(os.path.join(path,'new2.txt'),'w')

with open (os.path.join(path,'test.txt'),'r') as of:
    data = of.read()

data_1 = data [::-1]

new_file.write(data_1)

read_file = open(os.path.join(path,'new2.txt'),'r')
print(read_file.read())







