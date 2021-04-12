if __name__=="__main__":
    n=int(input())
    heigh=0
    while (2**heigh-1)<n:
        heigh+=1
    print(heigh)