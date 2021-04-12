class Sample:
    def get(self):
        global a,b
        print("Enter the Two Numbers ")
        a=int(input())
        b=int(input())
class Example(Sample):
    def display(self):
        global sum
        sum=a+b
        print("Sum  = ",sum)
obj=Example()
obj.get()
obj.display()
input()
