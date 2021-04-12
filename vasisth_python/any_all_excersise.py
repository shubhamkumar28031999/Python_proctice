def my_sum(*args):
    if all ([type(arg) == int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total +=num
        return total
    else:
        return "wrong input"


print(my_sum(1,2,10,4,3.4))
