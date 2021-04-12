if __name__=="__main__":
    num=int(input())
    arr=list(map(int,input().split()))
    max_len=1
    for i in range(num-2):
        temp_Arr=[arr[i]]
        t=0
        n=i+1
        while n<num