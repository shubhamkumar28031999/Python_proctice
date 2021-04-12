id=input("Enter the Employee Id        :  ")
name=input("Enter the Name of Employee :  ")
dsg=input("Enter the Designation       :  ")
basic=int(input("Enter the Basic Salary:  "))
l=int(input("Enter the Total Leaves   :  "))
lamount=basic/30*l
if(basic<=10000):
	ta=basic*2/100
	da=basic*3/100
	hra=basic*4/100
	ma=2500
else:
	ta=basic*5/100
	da=basic*6/100
	hra=basic*7/100
	ma=3500
gross=basic+ta+da+hra+ma
if(basic<=20000):
	itax=0
else:
	itax=(basic-20000)*5/100
net=gross-itax-lamount
print("---------Salary Slip----------")
print("Employee Id     :       ",id)
print("Name            :       ",name)
print("Designation     :       ",dsg)
print("------------------------------")
print("Leaves          :       ",l)
print("Leaves Amount   :       ",lamount)
print("------------------------------")
print("Ta\tDa\tHra\tMa")
print(ta,"\t",da,"\t",hra,"\t",ma)
print("------------------------------")
print("Gross Salary    :       ",gross)
print("Income Tax      :       ",itax)
print("Net Salary      :       ",net)
print("------------------------------")
input()
