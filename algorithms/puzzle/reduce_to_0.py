def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n
    return prime_factor


def check(n):
    count = 0
    while n != 0:
        max_prime=Largest_Prime_Factor(n)
        # print(f"n={n}     max_prime={max_prime}")
        if max_prime!=1:
            if max_prime==n:
                n = n - 1
                count += 1
            else:
                n = max_prime
                count += 1
        else:
            n=n-1
            count+=1
    return count


if __name__ == "__main__":
    n = int(input())
    print(check(n))
