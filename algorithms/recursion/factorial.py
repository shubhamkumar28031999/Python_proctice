def factorial(num1):
    if num1 == 1 or num1 == 0:
        return 1
    return num1 * factorial(num1 - 1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        num = int(input())
        num = factorial(num)
        print(num)
