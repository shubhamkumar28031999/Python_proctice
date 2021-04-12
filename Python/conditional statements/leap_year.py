year=int(input("Enter the Year number "))
if(year%100==0):
	if(year%400==0):
		print(year," is LeapYear")
	else:
		print(year," is not a LeapYear")
else:
	if(year%4==0):
		print(year," is LeapYear")
	else:
		print(year," is not a LeapYear")
input()