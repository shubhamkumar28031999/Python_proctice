class Student:
    def get_details(self):
        self.name=input("Enter the Name of Student :  ")
        self.roll=int(input("Enter the ROll Number     :  "))
        self.age=int(input("Enter the Age              :  "))
class Subject(Student):
    def get_subjects(self):
        self.p=int(input("Enter the Marks in Physics        :  "))
        self.c=int(input("Enter the Marks in Chemistry      :  "))
        self.m=int(input("Enter the Marks in Math           :  "))
        self.h=int(input("Enter the Marks in Hindi          :  "))
        self.e=int(input("Enter the Marks in English        :  "))
class Sports(Student):
    def get_sports(self):
        self.phy=int(input("Enter the Marks in Physical Education :  "))
class Result(Subject,Sports):
    def calculate(self):
        self.total=self.p+self.c+self.m+self.h+self.e
        self.avg=self.total/6
        if(self.avg>=90):
            self.grade="A+"
        elif(self.avg>=80):
            self.grade="A"
        elif(self.avg>=70):
            self.grade="A-"
        elif(self.avg>=60):
            self.grade="B+"
        elif(self.avg>=50):
            self.grade="B"
        elif(self.avg>=40):
            self.grade="B-"
        else:
            self.grade="FAIL"
    def display(self):
        print("----->>> Marksheet <<<---------")
        print("Roll Number        :      ",self.roll)
        print("Age                :      ",self.age)
        print("Name               :      ",self.name)
        print("--------------------------------")
        print("Physics            :      ",self.p)
        print("Chemistry          :      ",self.c)
        print("Math               :      ",self.m)
        print("Hindi              :      ",self.h)
        print("English            :      ",self.e)
        print("Physical Education :      ",self.phy)
        print("--------------------------------")
        print("Total              :      ",self.total)
        print("Average            :      ",self.avg)
        print("Grade              :      ",self.grade)
        print("--------------------------------")
s=Result()
s.get_details()
s.get_subjects()
s.get_sports()
s.calculate()
s.display()
input()






            
