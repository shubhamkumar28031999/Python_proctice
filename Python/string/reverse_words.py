str=input("Enter the String ")
length=len(str)
print("original String is :  ")
print(str)
s=""
for i in range(length-1,-1,-1):
	if(i==0 or str[i-1]==" "):
		for j in range(i,length):
			if(str[j]==" "):
				break
			else:
				s=s+str[j]
		s=s+" "
print("String in Reverse Order :  ")
print(s)
input()