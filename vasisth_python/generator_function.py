def nums(n):
    for i in range(1,n+1):
        yield i
for number in nums(10):
    print(number)

print("=======================")
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
for i in even(10):
    print(i)