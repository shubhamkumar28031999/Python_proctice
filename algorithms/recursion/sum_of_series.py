def sum_of_series(n):
    sum=0
    if n==1:
        return 1
    else:
        return n**n+sum_of_series(n-1)

if __name__=="__main__":
    print(sum_of_series(3))