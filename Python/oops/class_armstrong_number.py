class Sample:
	def sum_digit(self,num):
		sum=0
		while(num!=0):
			r=num%10
			sum=sum+r*r*r
			num=num//10
		return sum
n=int(input("Enter the Number : "))
obj=Sample()
s=obj.sum_digit(n)
if(s==n):
	print("Armstrong Number")
else:
	print("Not Armstrong Number")
input()