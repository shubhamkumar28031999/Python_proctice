def solve(arr,l):
    if l>=2:
        n=1
        b=1
        prev=arr[0]
        while b<l:
            if prev==arr[b]:
                pass
            else:
                prev=arr[b]
                n+=1
            b+=1
            # print(prev)
        return n

    else:
        return l



n=int(input())
arr=list(map(int,input().split()))
print(solve(arr,n))