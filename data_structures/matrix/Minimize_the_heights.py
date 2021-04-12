if __name__=="__main__":
    t= int(input())
    for i in range(t):
        k=int(input())
        n=int(input())
        arr= list(map(int,input().strip().split()))
        mid_arr=(max(arr)+min(arr))//2
        print(mid_arr)
        for i in range(len(arr)):
            if arr[i]==mid_arr:
                pass
            if arr[i]>mid_arr:
                # if arr[i]-mid_arr>=k:
                arr[i]=arr[i]-k
                # if arr[i]-mid_arr<k:
                #     diff=arr[i]-mid_arr
                #     arr[i]=arr[i]-diff
            else:
                # if mid_arr-arr[i]<k:
                #     diff=arr[i]-mid_arr
                #     arr[i]=arr[i]+diff
                # if mid_arr-arr[i]>=k:
                arr[i]=arr[i]+k
            print(arr)
        print(max(arr)-min(arr))

# 3
# 2
# 4
# 1 5 8 10


# 1
# 4
# 17 13 14 9