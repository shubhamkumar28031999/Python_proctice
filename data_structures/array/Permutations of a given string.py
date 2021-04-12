from itertools import permutations
if __name__=="__main__":
    for _ in range(int(input())):
        st=input()
        string=[]
        for i in range(len(st)):
            string.append(st[i])
        string.sort()
        p=permutations(string,len(st))
        for val in p:
            print("".join(val),end=" ")
        print()
