"""
str=input("Enter the String :  ")
length=len(str)
print("Original String is = ",str)
s=""
for i in range(0,length):
	s=str[i]+s
print("Reversed String is = ",s)
if(str==s):
	print("Palindomre")
else:
	print("Not Palindomre")
"""
str=input("Enter the String :  ")
length=len(str)
f=0
for i in range(0,(int(length/2)+1)):
	if(str[i] != str[length-1-i]):
		f=1
		break
if(f==0):
	print("Palindomre")
else:
	print("Not Palindomre")
input()