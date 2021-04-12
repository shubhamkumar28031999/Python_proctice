class Sample:
    def __init__(self):
        self.a,self.b
    def get(self):
        self.a=int(input("Enter Value of a "))
        self.b=int(input("Enter Value of b "))
    def display(self):
        self.sum=self.a+self.b
        print("Sum = ",self.sum)
class Example(Sample):
    def __init__(self):
        print("In Example Class")
obj=Example()
obj.get()
obj.display()
input()
              
