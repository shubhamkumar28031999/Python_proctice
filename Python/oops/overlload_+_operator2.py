class Sample:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def display(self):
        print(self.x,"\t",self.y)
        
    def __add__(self,other):
        obj=Sample()
        obj.x=self.x + other.x
        obj.y=self.y + other.y
        return obj
obj1=Sample(100,10)
obj2=Sample(200,20)
obj3=Sample()
obj3=obj1+obj2
#obj3=obj1.__add__(obj1,obj2)
obj3.display()
input()
