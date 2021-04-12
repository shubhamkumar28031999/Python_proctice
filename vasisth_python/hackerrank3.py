no=int(input(""))
for i in range(0,no):
    for j in range(0,no-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("#",end="")
    print("\n",end="")
