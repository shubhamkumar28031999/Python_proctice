class Outer:
    def display(self):
        print("In display function of Outer class")
        class Local:
            def show(self):
                print("In Show function of Local Class")
        x=Local()
        x.show()
    class Inner:
        def print_value(self):
            print("In Print_Value function of Inner Class")
obj=Outer()
obj.display()
y=Outer.Inner()
y.print_value()
input()
                      
