def isPalindrome(s):
    #s_rev = s[::-1]
    #boolean = bool(s == s[::-1])
    if (s == s[::-1]):
        return ("YES")
    else:
        return("NO")

def isPalindrome_2(s):
    w = ""
    for i in s:
        w = i + w
        if (s == w):
            return "YES"
    return "NO"
       
            

s = input("Enter string : ")
print(isPalindrome(s))
print(isPalindrome_2(s))