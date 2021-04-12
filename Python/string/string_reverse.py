str=input("Enter the String :  ")
length=len(str)
print("Original String is = ",str)
s=""
for i in range(0,length):
	s=str[i]+s
print("Reversed String is = ",s)
input()