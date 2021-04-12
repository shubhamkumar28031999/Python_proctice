import collections
class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        def find(u, s):
            if s[u] == u: return u
            s[u] = find(s[u], s)
            return s[u]

        def merge(u, v, s):
            s[find(u, s)] = s[find(v, s)]
            # print(s)

        ds = list(range(len(source)))
        for i in allowedSwaps:
            merge(i[0], i[1], ds)
        print(ds)
        start_pos = collections.defaultdict(list)
        for i in range(len(source)):
            start_pos[source[i]].append(i)
        print(start_pos)
        Hamming = 0
        for i in range(len(target)):
            prev = start_pos[target[i]]
            found = False
            for j in prev:
                if find(i, ds) == find(j, ds):
                    prev.remove(j)
                    found = True
                    break
            if not found: Hamming += 1

        return Hamming

source = [5,1,2,4,3]
target =[1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
s=Solution()
print(s.minimumHammingDistance(source,target,allowedSwaps))