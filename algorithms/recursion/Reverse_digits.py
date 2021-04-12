def reverseNumber(num):
    if num<1:
        return 0
    return (num%10)*10**(len(str(num))-1)+reverseNumber(num//10)


if __name__=="__main__":
    t= int(input())
    for i in range(t):
        number=int(input())
        num= reverseNumber(number)
        print(num)
