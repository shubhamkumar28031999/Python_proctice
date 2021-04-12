class Sample:
    def __init__(self):
        print("In Base Class i.e. Sample Class")
class Example(Sample):
    def __init__(self):
        super().__init__()
        print("In Derived Class i.e. Example Class")
obj=Example()
input()
