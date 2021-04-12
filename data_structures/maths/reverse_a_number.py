if __name__=="__main__":
    num=int(input())
    result=0
    while(num>0):
        remainder=num%10
        result=(result*10)+remainder
        num=num//10
    print(result)