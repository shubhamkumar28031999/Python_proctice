def LCS(arr1, arr2, n1, n2, dp):
    if n1 == 0 or n2 == 0:
        # print(f"n1 = {n1} and n2={n2}")
        return 0
    key = (n1, n2)

    if key not in dp:
        if arr1[n1] == arr2[n2]:
            dp[key] = LCS(arr1, arr2, n1 - 1, n2 - 1, dp) + 1
        else:
            dp[key] = max(LCS(arr1, arr2, n1, n2 - 1, dp), LCS(arr1, arr2, n1 - 1, n2, dp))
    # print(dp)
    return dp[key]+1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n1, n2 = list(map(int, input().strip().split()))
        arr1 = input()
        arr2 = input()
        dp = {}
        print(LCS(arr1, arr2, len(arr1)-1, len(arr2)-1, dp)+1)
