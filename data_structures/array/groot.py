def solve(s):
    counter={}
    count_1=0
    for i in s:
        if i!='?':
            if i not in counter:
                s[i]=1
            else:
                s[i]+=1
        elif i=='?':
            count_1+=1
    p=len(counter.values())
    if count_1>=26-p:
        return 1
    else:
        return -1
s=int(input())
print(solve(s))