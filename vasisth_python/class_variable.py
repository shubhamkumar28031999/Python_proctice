class circle:
    pi=3.14             #class variable
    def __init__(self,radius):
        self.radius=radius
    def calculate_circumference(self):
        return 2*circle.pi*self.radius
c=circle(5)
print(c.calculate_circumference())


circle.pi=1
print(c.calculate_circumference())
print(c.__dict__)