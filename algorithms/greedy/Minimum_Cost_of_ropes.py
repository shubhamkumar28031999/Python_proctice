if __name__ == "__main__":
    t = int(input())
    for a in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr.sort()

        for i in range(1,len(arr)):
            arr[i]= arr[i] +arr[i-1]

        print(sum(arr[1:]))
