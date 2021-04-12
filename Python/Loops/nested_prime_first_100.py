import math
c=0
num=2
while(c<100):
	f=0
	for i in range(2,int(math.sqrt(num))+1):
		if(num%i==0):
			f=1
			break
	if(f==0):
		print(num,end="\t")
		c=c+1
	num=num+1
print("\nTotal Prime Numbers = ",c)
input()