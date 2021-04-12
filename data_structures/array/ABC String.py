def valid(s):
    count=0
    for val in s:
        if val=="(":
            count+=1
        elif val==")":
            if count==0:
                return 0
            else:
                count-=1
    return count==0

def solve(s):
    f=s[0]
    l=s[-1]
    s=s.replace(f,"(")
    s=s.replace(l,")")
    mid=list({"A","B","C"}-{f,l})[0]
    if valid(s.replace(mid,"(")) or valid(s.replace(mid,")")):
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    s=input()
    print(solve(s))