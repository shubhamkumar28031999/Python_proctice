#Searching:
#linear search
a=input("Enter String :  ")
c=0
n=input("Enter the Charcater to count in String ")
for i in range(0,len(a)):
	if(a[i]==n):
		print(n," found at a[",i,"]")
		c=c+1
if(c==0):
	print(n," Does not Exist in List")
else:
	print("Total Result Found = ",c)
input()