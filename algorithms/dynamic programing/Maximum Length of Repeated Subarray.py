class Solution:
    def findLength(self, A, B):
        if A==B:
            return len(A)
        else:
            len_a = len(A)
            len_b = len(B)
            dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a+1)]
            ans = 0
            for i in range(len_a+1):
                for j in range(len_b+1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    else:
                        if A[i - 1] == B[j - 1]:
                            dp[i][j] = dp[i - 1][j - 1]+1
                            ans = max(ans, dp[i][j])
                        else:
                            dp[i][j] = 0
            for val in dp:
                print(val)
            return ans


if __name__ == "__main__":
    A = [0,0,0,0,1]

    B =[1,0,0,0,0]

    print(Solution().findLength(A, B))
