def permutations_with_repetition(s):
    base = len(s)
    for n in range(base**base):
        yield "".join(s[n // base**(base-d-1) % base] for d in range(base))

def product(x):
    final = [[]]
    l = len(x)
    groups = [list(x)] * l
    for i in groups:
        final = [x + [y] for x in final for y in i]
    for k in final:
        yield ''.join(k)


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

s=list("abs")
for p in permutation(s):
    print(p)


class Solution:
    def permuteUnique(self, nums):
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            dupcheck = []
            for i, x in enumerate(nums):
                if x not in dupcheck:
                    dfs(nums[:i] + nums[i + 1:], path + [x])
                    dupcheck.append(x)

        res = []
        dfs(nums, [])
        return res

    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                res.append(nums[::])
            else:
                for i in range(start, len(nums)):
                    nums[i], nums[start] = nums[start], nums[i]
                    backtrack(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]
        res = []
        backtrack(0)
        return res

a=[1,2,3]
s=Solution()
print(s.permute(a))