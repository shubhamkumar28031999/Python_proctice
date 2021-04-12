
def pattern(n):
    print(n,end=" ")
    if n<=0 :
        return n
    val=pattern(n-5)+5
    print(val,end=" ")
    return val



if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        pattern(n)
        print()