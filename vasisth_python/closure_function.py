def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power
cube = to_power(3)
print(cube(2))