num=int(input("Enter the Number :  "))
sum=0
while(num!=0):
	r=num%10
	sum=sum+r
	#num=int(num/10)
	num=num//10
print("Sum of Digits = ",sum)
input()