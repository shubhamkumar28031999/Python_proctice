print("Enter the Five Numbers :")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if(a<b and a<c and a<d and a<e):
	print(a," is Smallest")
elif(b<c and b<d and b<e):
	print(b," is Smallest")
elif(c<d and c<e):
	print(c," is Smallest")
elif(d<e):
	print(d," is Smallest")
else:
	print(e," is Smallest")
input()