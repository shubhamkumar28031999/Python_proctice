id=input("Enter the Employee Id        :  ")
name=input("Enter the Name of Employee :  ")
dsg=input("Enter the Designation       :  ")
basic=int(input("Enter the Basic Salary:  "))
l=int(input("Enter the Total Leaves   :  "))
lamount=basic/30*l
ta=basic*5/100
da=basic*6/100
hra=basic*7/100
ma=3500
gross=basic+ta+da+hra+ma
itax=basic*5/100
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
 
