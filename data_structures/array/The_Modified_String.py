def modified(s):
    number = 0
    i=0
    while i<(len(s)-2):
        same = 0
        j = i
        while j<len(s) and s[i] == s[j]:
            same += 1
            j += 1
        i = i +same
        number = number + (same - 1) // 2
    return number


num = int(input(""))
for i in range(num):
    s = str(input(""))
    print(modified(s))
