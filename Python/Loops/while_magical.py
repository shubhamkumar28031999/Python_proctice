num=int(input("Enter the number : "))
sum=0
original=num
while(num!=0):
	r=num%10
	sum=sum+r
	num=num//10
rev=0
num=sum
while(num!=0):
	r=num%10
	rev=rev*10+r
	num=num//10
if(sum*rev==original):
	print("Magical Number")
else:
	print("Not Magical Number")
input()
