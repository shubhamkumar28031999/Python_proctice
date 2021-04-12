def display(a):#actual parameter
    a=a+1
    print("In Display function")
    if(a<5):
        display(a)
    print("Back to display")
print("In Main")
display(0)
print("Back to main")
input()
