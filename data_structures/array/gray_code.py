def gray_code(n):
    arr=[]
    for i in range(1<<n):
        print(i>>1)
        arr.append(bin(i^(i>>1)).replace("0b",'').zfill(3))
    return arr
print(gray_code(3))
