a,b=2,3
def func():
    a=5
    global b
    b=10
    print(f"in function value of a is {a}")
    print(f"in function value of b is {b}")
    
func()
print(f"outside function vale of a is {a}")
print(f"outside function value of b is {b}")
