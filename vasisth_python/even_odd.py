def fun1(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
def fun2(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
def fun3(num):
    if num%2==0:
        return "even"
    return "odd"
def fun4(num):
    return num%2==0

num = int(input("enter any number"))
fun1(num)
print(fun2(num))
print(fun3(num))
print(fun4(num))