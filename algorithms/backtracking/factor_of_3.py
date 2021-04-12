from itertools import permutations

if __name__=="__main__":
    for _ in range(int(input())):
        k=int(input())
        arr=list(map(int,input().strip().split()))
        perm=permutations(arr)
        # list(perm)
        x = 1
        for tup in perm:

            for j in range(len(tup)-1):
                # print(f"tup[j]={tup[j]} and tup[j+1]={tup[j+1]}")
                y=1
                if tup[j]+tup[j+1]%3==0:
                    x= True
                    break
        if x:
            print("Yes")
        else:
            print("No")




