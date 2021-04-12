from functools import  wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """this is wrapper function"""
        print("hello world")
        return any_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def func(a):
    print(f"nice to meet u sir {a} times")
func(4)

@decorator_function
def add(a,b):
    """tjis add function"""
    return a+b
print(add(3,4))

print(add.__doc__)
print(add.__name__)



