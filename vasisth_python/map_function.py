numbers=[1,2,3,4,5,6]
def square(a):
    return a**2

# squares=list(map(square,numbers))
squares=list(map(lambda a:a**2,numbers))
print(squares)

#list comprihension
print([i**2 for i in numbers ])

new_list=[]
for num in numbers:
    new_list.append(square(num))

names=['shubham','kumar','sonal','nikhil','susmita']
length=list(map(len,names))
print(length)

