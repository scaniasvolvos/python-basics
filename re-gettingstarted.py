import re
'''
exp = re.compile('[a-e]')
print(exp.findall('this is a demo re'))

digit = re.compile('\d')
print(digit.findall("I met him at 11 AM on 10 Jan 2000"))

digit_group = re.compile('\d+')
print(digit_group.findall("I met him at 11 AM on 10 Jan 2000"))

#ip_re = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\$")
#ip_re = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
#print(ip_re.findall("IP address in 192.168.2.3"))
'''
sample = re.compile('\\W+')
print(sample.findall("##### &&&&&&& test %%%%"))


print(re.split("\\W+","words, word's', Words"))


vowels = re.compile('[aeiouAEIOU]')
print(vowels.findall("this is a aa test A test"))

mystr = "this is a demo"
serstr = "this"


if (mystr.find(serstr)):
    print("Present")
else:
    print("NP")

'''
if re.search(serstr,mystr):
    print("Present")
else:
    print("Not Present")
'''