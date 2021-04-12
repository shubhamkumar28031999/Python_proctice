class Sample:
    def display(self):
        print("In Base Class i.e. Sample Class")
class Example(Sample):
    def show(self):
        print("In Derived Class i.e. Example Class")
obj=Example()
obj.display()
obj.show()
input()
