num=int(input("Enter the Number :  "))
sum=0
for i in range(1,num//2+1):
	if(num%i==0):
		sum=sum+i
if(sum==num):
	print("Perfect Number")
else:
	print("Not Perfect Number")
