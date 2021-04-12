number1=[2,4,6,8,10]
number2=[1,2,3,4,5,6,7,8]
even1=[]
for i in number1:
    even1.append(i%2==0)
print(even1)
print(all(even1))
print(any(even1))
even2=[]
for i in number2:
    even2.append(i%2==0)
print(even2)
print(all(even2))
print(any(even2))


# in one line
print("------------in one line--------------------")
print(all(num%2==0 for num in number2))