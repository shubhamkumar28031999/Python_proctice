def GenerateBinary(n):
    for i in range(1,n+1):
        print(int(bin(i).replace("0b",'')),end=" ")

GenerateBinary(6)
