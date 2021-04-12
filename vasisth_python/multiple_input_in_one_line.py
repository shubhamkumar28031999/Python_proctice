name,age=input('enter your name and age').split(' ')
print(f"hello Mr. {name} and your age is {age}")
print(name[::-1])

#average
num1,num2,num3 = input('enter any three numbers').split(' ')


print(f"average of {num1} , {num2} and {num3} is {((int(num2)+int(num1)+int(num3))/3)}")