from itertools import chain, combinations
def powerset(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1))
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(str,input().strip().split()))
        arr2=[]
        for val in list(powerset(arr)):
            st=sorted(val)
            if st not in arr2:
                arr2.append(st)

        for val in sorted(arr2):
            z=" ".join(val)
            print("("+z+")",end="")
        print()


