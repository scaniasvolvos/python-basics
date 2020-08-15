
Input = [[[3], [4]], [[5], [6]], [[7], [8]]] 

result = []

for i in Input:
    for j in i:
        result.append(j)
print (result)



'''
# Python code to convert a 3D list into a 2D list 
  
# Input list initialization 
Input = [[[3], [4]], [[5], [6]], [[7], [8]]] 
  
# Output list initialization 
Output = [] 
  
# Using iteration 
for temp in Input: 
    for elem in temp: 
        Output.append(elem) 
  
# printing output 
print("Initial 3d list is") 
print(Input) 
print("Converted 2d list is") 
print(Output) 
'''