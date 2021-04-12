class Employee:
	def init(self):
                self.id
                self.basic
                self.name
	def get(self):
		self.id=int(input("Enter the Employee ID     : "))
		self.basic=int(input("Enter the basic Salary : "))
		self.name=input("Enter the Name              : ")
	def display(self):
		print("Name         = ",self.name)
		print("Id           = ",self.id)
		print("Basic Salary = ",self.basic)
obj=Employee()
obj.get()
obj.display()
input()
