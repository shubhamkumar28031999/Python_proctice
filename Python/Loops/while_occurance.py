num=int(input("Enter the Number :  "))
d=int(input("Enter the Digit to Count :  "))
c=0
while(num!=0):
	r=num%10
	num=num//10
	if(d==r):
		c=c+1
print(d," Exist ",c," times in number")
input()