class Base:
    def get(self):
        global a
        print("Enter Elements in List  : ")
        a=[int(x) for x in input().split()]
class Derived1(Base):
    def display(self):
            print(a)
class Derived2(Derived1):
    def sort(self):
        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                if(a[i]>a[j]):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
obj=Derived2()
obj.get()
print("Original List is :")
obj.display()
obj.sort()
print("Sorted List is :")
obj.display()
