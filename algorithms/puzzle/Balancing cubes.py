if __name__ == "__main__":
    n = int(input())
    ans = 0
    if n % 2 != 0:
        while n != 1:
            n = int(n / 3) + 1
            ans += 1
    else:
        while n != 1:
            n = int(n / 2)
            ans += 1
    print(ans)
