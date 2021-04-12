from itertools import permutations
def number_of_ways(n):
    l=len(n)
    arr=permutations(n,l)
    s=[]
    for val in arr:
        temp=list(val)
        t1=sorted(temp[:l//2])
        t2=sorted(temp[l // 2:])
        if t1 in s:
            pass
        else:
            s.append(t1)
        if t2 in s:
            pass
        else:
            s.append(t2)
        # s.add(temp[:l//2])
        # s.add(temp[l // 2:])
    print(len(s)//2)

if __name__=="__main__":
    n=[x for x in range(1,int(input())+1)]
    number_of_ways(n)