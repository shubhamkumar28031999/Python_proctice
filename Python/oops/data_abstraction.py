class Sample:
    def __init__(self,x):
        self.__a=x
    def display(self):
        print("a = ",self.__a)
obj=Sample(10)
#print(obj.__a)
obj.display()
input()
