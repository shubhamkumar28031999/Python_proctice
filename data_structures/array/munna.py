n=5
i=0
k=0

for i in range(n+1):
    for j in range(1,k+1):
        print("#")
    if i>n/2:
        k=k-3
    else:
        k=k+1
        print()
