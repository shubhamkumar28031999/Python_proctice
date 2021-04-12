def fab(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return (fab(num-1)+fab(num-2))

num=int(input("enter any number"))
for i in range(num):
    print(str(fab(i))+",",end="")



