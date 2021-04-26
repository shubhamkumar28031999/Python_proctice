for _ in range(int(input())):
    S,N,M=map(int,input().split())

    val=0
    buy=0
    cnt=0
    while val<S:
        if buy>=M:
            val+=buy//M
            buy-=val*M
        else:
            while buy<M:
                cnt+=1
                buy+=N
    if cnt<=S:
        print(cnt)
    else:
        print(-1)