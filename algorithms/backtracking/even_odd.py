def product(*args, **kwds):
    pools = list(args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    count=0
    for i in range(len(result)):
        if sum(result[i])%2==0:
            count+=1
    return count


low,high=map(int,input().split())
k=int(input())
lst=[i for i in range(low,high+1)]
print(product(lst,repeat=k))
