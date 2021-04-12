for _ in range(int(input())):
    n=int(input())
    number=0
    flag=9
    for i in range(n):
        number=number*10 + flag
        flag-=1
        if flag==-1:
            flag=9
    print(number)