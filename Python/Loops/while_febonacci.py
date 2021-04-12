#febonacci Series: 0 1 1 2 3 5 8 13 21 34 55 89 144..........
a=0
b=1
sum=a+b#initialization
num=int(input("Enter the Last Term Range :  "))#initialization
print(a,"\t",b,end="\t")
while(sum<=num):#condition
	print(sum,end="\t")
	a=b		#updation
	b=sum	#updation
	sum=a+b	#updation
input()
