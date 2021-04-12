numbers=[1,2,3,4]#iterabels
squares=map(lambda a:a%2==0,numbers)#iterator

numbers_iter=iter(numbers)
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print((list(iter(numbers))))
print(next(squares))
print(next(squares))
print(next(squares))