x=0
y=9
for i in range(1,6):
	x=y
	for j in range(1,i+1):
			print(x,end="")
			x=x-1
	print()
	y=y-1
input()
