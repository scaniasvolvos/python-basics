def rev_sentence(sentence):
    words = sentence.split(' ')
    rev_sent = ' '.join(reversed(words))
    return rev_sent

def rev_chars(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        rev_word = ''.join(reversed(words[i]))
        print(rev_word,end=' ')

def rev_word(input_word):
    #inp_str = input_word.split(' ')
    str =""
    for i in input_word:
        str = i + str
    return str

def main():
    input = 'this is a test line'
    input_word = 'pranav'
    print(rev_word(input_word))
    print (rev_sentence(input))
    #rev_chars(input)
if __name__ == "__main__":
    main()
    