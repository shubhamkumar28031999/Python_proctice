def AVT(mat):
    TAT=0
    n=0
    start_time=0
    for val in mat:
        n+=1
        if val[0]>=start_time:
            TAT+=val[1]
            start_time=val[1] + val[0]
        else:
            TAT+=start_time-val[0]+val[1]
            start_time+=val[1]
        print(TAT)
    # print(TAT)
    TAT=TAT
    print(TAT/n)

customers = [[1,2],[2,5],[4,3]]
AVT(customers)


