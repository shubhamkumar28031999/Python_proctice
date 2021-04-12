a=5#global
def display():
    a=10#local
    print("In display function a = ",a)
def show():
    a=20#local
    print("In Show function a = ",a)
def function():
    global a
    a=30
    print("In function a = ",a)
display()
show()
function()
input()
