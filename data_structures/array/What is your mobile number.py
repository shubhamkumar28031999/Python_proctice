def solve(s,l):
    if l!=10:
        return "NO"
    if s[0]=="0":
        return "NO"
    if s.isnumeric():
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    s=input()
    l=len(s)
    print(solve(s,l))