def min_num_of_jumpus(arr,len_arr):
    jumps=[0 for i in range(len_arr)]
    if len_arr==0 or arr[0]==0:
        return -1
    else:
        for i in range(1,len_arr):
            jumps[i]=float('inf')
            for j in range(i):
                if i<=j+arr[i] and jumps[j]!=float('inf'):
                    jumps[i]=min(jumps[i],jumps[j]+1)
                    break
        print(jumps)
        return jumps[-1]

# 2 3 1 1 2 4 2 0 1 1

if __name__=="__main__":
    for _ in range(int(input())):
        len_arr= int(input())
        arr=list(map(int,input().strip().split()))
        print(min_num_of_jumpus(arr,len_arr))