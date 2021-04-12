c=0
for num in range(1000,50000):
	rev=0
	temp=num
	while(temp!=0):
		r=temp%10
		rev=rev*10+r
		temp=temp//10
	if(num==rev):
		print(num,end="\t")
		c=c+1
print("\nTotal Palindrome Numbers = ",c)
input()