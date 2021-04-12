even=0
odd=0
for i in range(1,50001):
	if(i%2==0):
		even=even+i
	else:
		odd=odd+i
print("Sum of Even Numbers = ",even)
print("Sum of Odd Numbers = ",odd)
input()