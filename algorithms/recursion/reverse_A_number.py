def rev_number(num):
    if num>9:
        return (10**(len(str(num))-1))*(num%10)+rev_number(num//10)
    return num


if __name__=="__main__":
    print(rev_number(45912))