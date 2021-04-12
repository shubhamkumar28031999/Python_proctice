num=int(input("Enter the Number of Rows :  "))
for i in range(1,num+1):
	for j in range(1,num+1):
		if(i==1):
			print(j,end=" ")
		elif(i==num):
			print(num+1-j,end=" ")
		elif(j==1):
			print(i,end=" ")
		elif(j==num):
			print(num+1-i,end=" ")
		elif(i==j or i+j==num+1):
			if(i<=num/2):
				print(j,end=" ")
			else:
				print(num+1-j,end=" ")
		else:
			print(" ",end=" ")
	print()
input()