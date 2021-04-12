def solve(x,y,s):
    l = len(s)
    d = {"R": 0, "U": 0, "D": 0, "L": 0}
    for i in range(l):
        d[s[i]] += 1
    if x > 0:
        if d["R"] < x:
            return "NO"
    if x<0:
        if d["L"] < -1*x:
            return "NO"
    if y>0:
        if d["U"]<y:
            return  "NO"
    if y<0:
        if d["D"]<-1*y:
            return "NO"
    return "YES"
for _ in range(int(input())):
    x,y=map(int,input().split())
    s=input()
    print(solve(x,y,s))


