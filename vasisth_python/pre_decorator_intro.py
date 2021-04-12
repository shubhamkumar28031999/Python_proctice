def square(a):
    return a**2

s= square
print(s.__name__)
print(square.__name__)
print(s)
print(square)
print(square(4))
print(s(4))