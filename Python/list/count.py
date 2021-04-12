#count():used to calculate occurance of any element in list
a=[10,20,30,40,50,10,10,10,20]
n=int(input("Enter the Number to count in list "))
print(n," Exist ",a.count(n)," times in list")
"""
a=[10,20,30,40,50,10,10,10,20]
c=0
n=int(input("Enter the Number to count in list "))
for i in range(0,len(a)):
	if(a[i]==n):
		c=c+1
print(n," exist ",c," times in list")
"""
input()