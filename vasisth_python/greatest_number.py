def greater(a,b,c):
    if a>b and a>c:
        print ("a is greatest")
    if b>a and b>c :
        print ("b is greatest")
    else:
        print("c is greatest")

def greater2(a,b):
    if a > b:
        return a
    return b

def greatest3(a,b,c):
    return greater2(greater2(a,b),c)


a,b,c=[int() for a in input("enter any three numbers").split(" ")]

greater(a,b,c)
print(greatest3(a,b,c))