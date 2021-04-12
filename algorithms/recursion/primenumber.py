def prime(num,i=2):
    if num<=2:
        if num==2:
            return True
        else:
            return False
    if num%i==0:
        return False
    if i*i>num:
        return True
    return prime(num,i+1)



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        num = int(input())
        if prime(num):
            print("yes")
        else:
            print("No")