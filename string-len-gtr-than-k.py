def string_k(str, k):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string




str = "this is test string"
k = 4
print(string_k(str, k))