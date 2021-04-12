def print_formatted(number):
    for number in range(1, number + 1):
        octal = oct(number)
        hexa = hex(number)
        binary = bin(number)
        print(str(number)+"\t"+str(octal[2:])+"\t"+str(hexa[2:])+"\t"+str(binary[2:]))
n = int(input())
print_formatted(n)


