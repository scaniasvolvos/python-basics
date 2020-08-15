def omit(list1, word, occr):
    count = 0
    index = 0
    for i in list1:
        index += 1
        if i == word:
            count += 1
            if count == occr:
                list1.pop(index-1)
    return list1


list1 = ["he", "is", "ankit", "is", "raj", "is","ankit raj"] 
word="is"
n1=3

print("List after removing nth occurance ",omit(list1,word,n1))