def decorator_function(any_function):
    def wrapper_function():
        print("hello world!!")
        any_function()
    return wrapper_function
def func1():
    print("this is function 1")

def func2():
    print("this is function 2")

var= decorator_function(func1)
var()
print("---------------------------------------------------")

@decorator_function
def func3():
    print("this is function 1")
func3()
@decorator_function
def func2():
    print("this is function 2")
func2()