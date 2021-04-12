str=input("Enter the String :  ")
j=len(str)-1
print("Original String is = ",str)
i=0
temp=""
while(i<j):
	temp=str[i]
	str=str.replace(str[i],str[j])
	str=str.replace(str[j],temp)
	i=i+1
	j=j-1
print("Reversed String is = ",str)
input()