c=0
for i in range(19,1000):
	if(i%19==0):
		print(i,end="\t")
		c=c+1
print("\nTotal Multiples of 19 = ",c)
input()