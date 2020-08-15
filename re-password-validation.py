# importing re library 
import re 
  
def main(): 
    passwd = 'eek23'
    #reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?=&])[A-Za-z\d@$!#%*?&]{6,20}$"
    rege = "[A-Za-z\\d@$!#%*?&]{6,20}$"
      
    # compiling regex 
    pat = re.compile(rege) 
      
    # searching regex                  
    mat = re.search(pat, passwd) 
      
    # validating conditions 
    if mat: 
        print("Password is valid.") 
    else: 
        print("Password invalid !!") 
  
# Driver Code      
if __name__ == '__main__': 
    main() 