class Solution:
    def countArrangement(self, N):
        all = (1 << N) - 1
        an = [0] * all

        def permutation(tmp, k, ans):
            print(ans)
            if tmp == all:
                return 1
            if ans[tmp] > 0:
                return ans[tmp]
            score = 0
            for i in range(1, N + 1):
                if (tmp & (1 << (i - 1))) == 0:
                    if (k % i == 0) or (i % k == 0):
                        score += permutation(tmp + (1 << (i - 1)), k + 1, ans)
            ans[tmp] = score
            print(tmp)
            return score
        score = permutation(0, 1, an)
        return score

s=Solution()
print(s.countArrangement(4))