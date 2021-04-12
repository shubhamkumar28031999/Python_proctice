def display(a=0):#Formal parameter
    a=a+1
    print("In Display function")
    if(a<5):
        display(a)
    print("Back to display")
print("In Main")
display()
print("Back to main")
input()
