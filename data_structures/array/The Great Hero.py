def solve(A,B,n,attack_monster,initial_power):
    temp=[]
    for i in range(n):
        temp.append([attack_monster[i],initial_power[i]])
    temp=sorted(temp)
    for i in range(n):
        attack_monster[i]=


for _ in range(int(input())):
    A,B,n=map(int,input().split())
    attack_monster=list(map(int,input().split()))
    initial_power=list(map(int,input().split()))
    print(solve(A,B,n,attack_monster,initial_power))
