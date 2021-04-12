class Base1:
    def get1(self):
        global a,b
        print("Enter the Two Numbers in Class Base1 :  ")
        a=int(input())
        b=int(input())
class Base2:
    def get2(self):
        global c,d
        print("Enter the Two Numbers in Class Base1 :  ")
        c=int(input())
        d=int(input())
class Derived(Base1,Base2):
    def display(self):
        global sum
        sum=a+b+c+d
        print("Sum = ",sum)
obj=Derived()
obj.get1()
obj.get2()
obj.display()
input()
