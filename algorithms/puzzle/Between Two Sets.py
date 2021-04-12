import math
#
# def LCMofArray(a):
#   lcm = a[0]
#   for i in range(1,len(a)):
#     lcm = lcm*a[i]//math.gcd(lcm, a[i])
#   return lcm
def getTotalX(a, b):
    count=100000007
    for val_a in a:
        count_in=0
        for val_b in b:
            if val_b%val_a==0:
                count_in+=1
        count=min(count_in,count)
    return count

a=[100,99,98,97,96,95,94,93,92,91]
b=[1,2,3,4,5,6,7,8,9,10]
print(getTotalX(a,b))
