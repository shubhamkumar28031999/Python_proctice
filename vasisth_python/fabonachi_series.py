fibs=[0,1]
n=int(input("enter the number"))
for i in range(n):
    fibs.append(fibs[-1]+fibs[-2])
print(fibs)

y=[fibs.append(fibs[-1]+fibs[-2]) for i in range(n)]
print(y)