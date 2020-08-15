def vowel_count(str):
    count  = 0
    vowel = set("aeiouAEIOU")
    str = str.split(' ')
    for i in range(len(str)):
        for alphabet in str[i]:
            if alphabet in vowel:
                count += 1
    print ("The string {0} has count {1}".format(str,count))
str = "voweltest this is a"
vowel_count(str)