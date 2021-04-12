import sys
def minIndexChar(str,p):
    s = set(str)
    p = set(p)
    itersect = list(s.intersection(p))
    if itersect == []:
        return -1
    else:
        index= sys.maxsize
        for j in range(len(itersect)):
            for i in range(len(str)):
                if str[i] == itersect[j]:
                    if index>i:
                        index = i
                    else:
                        pass
                else:
                    continue
        return index
# hasjkhflaskdf
# sdlkjfshd

num = int(input(""))
for i in range(num):
    s = input("")
    p = input("")
ans = minIndexChar(s,p)
if ans == -1:
    print("No character present")
else:
    print(s[ans])