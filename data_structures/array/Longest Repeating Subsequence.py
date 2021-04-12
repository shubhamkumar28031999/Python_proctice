from collections import Counter
if __name__=="__main__":
    for _ in range(int(input())):
        num=int(input())
        st=input()
        length=len(st)
        l=1
        for i in range(length):
            j=i+1
            while j<length and st[i]==st[j]:
                j+=1
                # print(j)
            l=max(l,j-i)


        print(l)


