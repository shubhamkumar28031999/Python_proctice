class Solution:

    def solve(self, candidates, target, result, unique, i=0, current=[]):
        if target == 0:
            temp = [i for i in current]
            if tuple(temp) not in unique:
                unique[tuple(temp)] = 1
                result.append(temp)
            return
        elif target < 0:
            return
        else:
            for x in range(i, len(candidates)):
                current.append(candidates[x])
                self.solve(candidates, target - candidates[x], result, unique, i, current)
                current.pop()

    def combinationSum(self, candidates, target):
        result = []
        unique = {}
        candidates = sorted(list(set(candidates)))
        self.solve(candidates, target, result, unique)
        return result

    def combinationSum2(self, candidates, target):
        result = []
        temp = []
        candidates.sort()

        def recur(k, t):
            for i in range(k, len(candidates)):
                temp.append(candidates[i])
                print(candidates[i])
                if t == candidates[i]:
                    result.append(temp[:])
                    del temp[-1]
                    return
                elif t > candidates[i]:
                    recur(i, t - candidates[i])
                    del temp[-1]
                elif t < candidates[i]:
                    del temp[-1]
                    return
        recur(0, target)
        return result

ob1 = Solution()
print(ob1.combinationSum2([2,3,6,7,8],10))