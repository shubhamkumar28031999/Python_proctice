numbers=[1,2,3,4,5]
x=[]

for i in range(len(numbers)):
    x.append(numbers.pop())
print(x)