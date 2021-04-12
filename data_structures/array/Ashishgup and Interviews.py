import math
def solve(arr,n,k):
    min_ques=math.ceil(n/2)
    bot=True
    answerd=0
    for val in arr:
        if val >-1:
            answerd+=1
    if answerd<min_ques:
        return "Rejected"
    for val in arr:
        if val>=2 or val==-1:
            bot=False
    if bot:
        return "Bot"
    for val in arr:
        if val > k:
            return "Too Slow"
    return "Accepted"


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(solve(arr,n,k))