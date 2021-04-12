import math
num=int(input("Enter the Number :   "))
f=0
for i in range(2,int(math.sqrt(num))+1):
	if(num%i==0):
		f=1
		break
if(f==0 and num>=2):
	print(num," Is prime")
else: 		
	print(num," Is not Prime")
input()