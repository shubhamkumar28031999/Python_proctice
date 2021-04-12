def longest_common_subsequence(arr_a,arr_b,len_a,len_b):
    if (len_a==0 or len_b==0):
        return 0
    if arr_a[len_a-1]==arr_b[len_b-1]:
        return 1+longest_common_subsequence(arr_a,arr_b,len_a-1,len_b-1)
    else:
        return max(longest_common_subsequence(arr_a,arr_b,len_a,len_b-1),longest_common_subsequence(arr_a,arr_b,len_a-1,len_b))


def lcs(X, Y,m,n):
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
            print(L)
    return L[m][n]

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"

    # Find the length of string
    m = len(X)
    n = len(Y)

    print("Length of LCS:",lcs(X, Y, m, n))

