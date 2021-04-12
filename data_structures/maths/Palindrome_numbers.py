if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        num = int(input())
        binary = bin(num).split("b")[1]

        if len(binary) % 2 == 0:
            left=binary[:len(binary)//2]
            right=binary[len(binary)//2:]
            if left==right[::-1]:
                print(1)
            else:
                print(0)
        else:
            left = binary[:len(binary) // 2]
            right = binary[len(binary)//2+1:]
            if left == right[::-1]:
                print(1)
            else:
                print(0)

