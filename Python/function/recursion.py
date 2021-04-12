def display():
    global a
    a=a+1
    print("In Display function")
    if(a<5):
        display()
    print("Back to display")
a=0
print("In Main")
display()
print("Back to main")
input()
