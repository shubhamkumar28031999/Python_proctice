def solve(s):
    arr=list(s)
    l=len(s)
    for i in range(l):
        if i%2==0:
            if arr[i]=="a":
                arr[i]='b'
            else:
                arr[i]='a'
        else:
            if arr[i]=="z":
                arr[i]="y"
            else:
                arr[i]='z'
    return "".join(arr)
for _ in range(int(input())):
    s=input()
    print(solve(s))
