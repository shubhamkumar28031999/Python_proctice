class Employee:
    cmp="Ducat"
    def __init_(self):
        self.id,self.basic,self.ta,self.da,self.hra,self.ma
        self.gross,self.itax,self.l,self.lamount,self.net
        self.dsg,self.name
    def get(self):
        self.id=int(input("Enter the Employee Id   :   "))
        self.name=input("Enter the Name            :   ")
        self.dsg=input("Enter the Designation   :   ")
        self.basic=int(input("Enter the Basic Salary :   "))
        self.l=int(input("Enter the Total Leaves :   "))
        if(self.basic<=10000):
            self.ta=self.basic*3/100
            self.da=self.basic*4/100
            self.hra=self.basic*5/100
            self.ma=2500
        else:
            self.ta=self.basic*6/100
            self.da=self.basic*7/100
            self.hra=self.basic*8/100
            self.ma=4500
        self.gross=self.basic+self.ta+self.da+self.hra+self.ma
        self.lamount=self.basic/30*self.l
        if(self.basic<=20000):
            self.itax=0
        else:
            self.itax=(self.basic-20000)*5/100
        self.net=self.gross-self.itax-self.lamount
    def display(self):
        print("---------Salary Slip----------")
        print("Employee Id     :       ",self.id)
        print("Name            :       ",self.name)
        print("Designation     :       ",self.dsg)
        print("Company Name    :       ",self.cmp)
        print("------------------------------")
        print("Leaves          :       ",self.l)
        print("Leaves Amount   :       %.2f"%self.lamount)
        print("------------------------------")
        print("Ta\tDa\tHra\tMa")
        print("%.2f\t%.2f\t%.2f\t%.2f"%(self.ta,self.da,self.hra,self.ma))
        print("------------------------------")
        print("Gross Salary    :       ",self.gross)
        print("Income Tax      :       ",self.itax)
        print("Net Salary      :       %.2f"%self.net)
        print("------------------------------")              
obj=Employee()
obj.get()
obj.display()
input()









        
        
        
