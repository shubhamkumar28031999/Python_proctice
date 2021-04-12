#Searching:
#linear search
print("Enter Element in List\n")
a=[int(x) for x in input().split()]
c=0
n=int(input("Enter the Number to count in list "))
for i in range(0,len(a)):
	if(a[i]==n):
		print(n," found at a[",i,"]")
		c=c+1
if(c==0):
	print(n," Does not Exist in List")
else:
	print("Total Result Found = ",c)
input()