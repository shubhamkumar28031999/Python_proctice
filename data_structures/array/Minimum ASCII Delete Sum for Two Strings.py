import collections
class Solution:
    def minimumDeleteSum(self, s1, s2):
        n=len(s1)
        m=len(s2)
        dp=[[0 for x in range(m+1)] for x in range(n+1)]
        print(dp)
        for i in range(n+1):
            for j in range(m+1):
                if i==0 and j==0: continue
                elif i==0:  dp[i][j] += (dp[i][j-1] + ord(s2[j-1]))
                elif j == 0: dp[i][j] += (dp[i-1][j] + ord(s1[i - 1]))
                elif s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1];
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]))
        return dp[n][m]




if __name__=="__main__":
    s1 = "delete"
    s2 = "leet"
    print(max(s1,s2))
    print(Solution().minimumDeleteSum(s1,s2))