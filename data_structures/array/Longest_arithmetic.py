def longest(arr,l):

    if l<=2:
        return 2
    else:

        d=arr[1]-arr[0]
        a=0
        max_length = 0
        for i in range(1,l):
            if arr[i]-arr[i-1]==d:
                a+=1
            else:
                max_length=max(max_length,a)
                a=1
                d=arr[i]-arr[i-1]
        max_length=max(max_length,a)+1
        return max_length





if __name__=="__main__":
    for k in range(int(input())):
        arr_len=int(input())
        arr=list(map(int,input().strip().split()))


        print("Case #" + str(k+1) + ": " + str(longest(arr,arr_len)))

