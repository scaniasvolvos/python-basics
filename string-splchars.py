import re

def splCharsTest(str):
    regex = re.compile(r'[@_!#$%^&*()<>?|/\}{~:]')
    if(regex.search(str) == None):
        print("String is accepeted")
    else:
        print("String is not accepted")

def manual_chartest(str):
    spl_chars = ['@','$','#','(',')']
   # count = len(spl_chars)
    for i in spl_chars:
        if i in str:
            print("Invalid")
            return 
    print("Valid")

if __name__ == "__main__":
    str = "test123@"
    splCharsTest(str)
    manual_chartest(str)
    