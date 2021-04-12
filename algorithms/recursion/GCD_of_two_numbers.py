
def GCD(num1,num2):
    if num1%num2==0:
        return num2
    return GCD(num2,num1%num2)


if __name__=="__main__":
    t= int(input())
    for i in range(t):
        num1,num2=list(map(int,input().strip().split()))
        num= GCD(num1,num2)
        print(num)
