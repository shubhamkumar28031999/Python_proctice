class Sample:
    def __init__(self,x=0):
        self.x=x
    def __add__(self,other):
        m=self.x + other.x
        return m
obj1=Sample(100)
obj2=Sample(200)
print(obj1+obj2)
input()
