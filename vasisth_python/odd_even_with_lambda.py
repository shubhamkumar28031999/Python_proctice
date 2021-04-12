num= int(input('enter any number'))
a= lambda num : num%2==0
print(a(num))
val=lambda num:print("even") if num%2==0 else print("odd")
print(val(num))