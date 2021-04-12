"""
#sum(): used to calculate sum of Element of a list(Deprecated)
a=[10,20,30,40,50]
print("Sum of Elements of list = ",a.sum())
"""
a=[10,20,30,40,50]
sum=0
for i in range(0,len(a)):
	sum=sum+a[i]
print("Sum of Elements of list = ",sum)
input()
