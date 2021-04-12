#compate two list
a=[1,2,3]
b=[1,2,3,4]
f=0
i=0
while(i<len(a)):
	if(a[i]!=b[i]):
		f=1
		break
	i=i+1
if(f==0 and len(a)==len(b)):
	print("Both List are Same")
else:
	print("Both List are not same")
input()