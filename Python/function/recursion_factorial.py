def fact(num):
    if(num<=0):
        return 1
    else:
        return num*fact(num-1)
n=int(input('Enter the number to get Factorial '))
f=fact(n)
#print("Factorial of ",n," is = ",f)
print("Factorial of %d is = %d"%(n,f))
input()
