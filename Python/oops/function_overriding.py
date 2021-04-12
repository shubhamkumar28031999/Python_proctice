class Sample:
    def display(self):
        print("In Display function of Sample class")
class Example(Sample):
    def display(self):
        print("In Display function of Example class")
        super().display()
x=Example()
x.display()
input()
