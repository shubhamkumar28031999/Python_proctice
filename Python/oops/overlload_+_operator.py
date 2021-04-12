class Sample:
    def __init__(self,x=0):
        self.x=x
    def display(self):
        print(self.x)
    def __add__(self,other):
        obj=Sample()
        obj.x=self.x + other.x
        return obj
obj1=Sample(100)
obj2=Sample(200)
obj3=Sample()
obj3=obj1+obj2
#obj3=obj1.__add__(obj1,obj2)
obj3.display()
input()
