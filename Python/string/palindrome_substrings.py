str=input("Enter the String :  ")
length=len(str)
c=0
for i in range(0,length):
	for j in range(i+2,length):
		temp=""
		for k in range(i,j+1):
			temp=temp+str[k]
		x=len(temp)
		f=0
		for k in range(0,int(x/2)):
			if(temp[k]!=temp[x-1-k]):
				f=1
				break
		if(f==0):
			print(temp)
			c=c+1
print("Total Palindrome Strings are :  ",c)
input()