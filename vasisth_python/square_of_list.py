def square(num):
    return num**2

square_list=[]
numbers=[1,2,3,4,5]

for i in numbers:
    square_list.append(square(i))

print(square_list)