num=int(input("Enter the Number of Rows :  "))
for i in range(1,num+1):
	for j in range(1,num+1):
		if(i==1 or i==num or j==1 or j==num or i==j or i+j==num+1):
			print("* ",end="")
		else:
			print("  ",end="")
	print()
input()