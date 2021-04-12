if __name__=="__main__":
    n,m=map(int,input().split())
    R=[]
    G=[]
    B=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        R.append(a)
        G.append(b)
        B.append(c)
    R_max=max(R)
    G_max=max(G)
    B_max=max(B)

    for _ in range(m):
        R_req,G_req,B_req=map(int,input().split())
        if R_req==R_max and G_req==G_max and B_req==B_max:
            print("YES")
        else:
            print("NO")


# 2 2
# 1 3 5
# 5 3 1
# 5 3 5
# 3 3 3