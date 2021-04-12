num = int(input("enter any number"))
num1=num
sum = 0
while num != 0:
    sum = num%10 + sum
    num = int(num/10)
print(f"sum is {sum}")

print ("by another method using string")
num1 = str(num1)
i = 0
sum1=0
print(num1)
while i < len(num1):
    sum1 = sum1 + int(num1[i])
    i+=1
print(f"sum by another method is {sum1}")