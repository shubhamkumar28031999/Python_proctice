if __name__=="__main__":
    t=int(input())
    for i in range(t):
        num = int(input())
        factorial=1
        for i in range(1,num+1):
            factorial*=i

        factorial=str(factorial)[::-1]

        count=0

        while factorial[count]=='0':
            count+=1

        print(count)