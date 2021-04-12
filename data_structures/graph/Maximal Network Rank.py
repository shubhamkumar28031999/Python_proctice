from itertools import combinations
class Solution:
    def maximalNetworkRank(self, n, roads):
        road_num = len(roads)
        cities = [0 for x in range(n + 1)]
        result = 0
        for x, y in roads:
            cities[x] += 1
            cities[y] += 1
            # print(cities)
        indices=combinations([x for x in range(len(cities))],2)
        for x,y in indices:
            if [x,y] in roads or [y,x] in roads:
                result = max(result, cities[x] + cities[y] - 1)
            else:
                result = max(result, cities[x] + cities[y])
        return result





if __name__=="__main__":
    roads =  [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    n=8
    print(Solution().maximalNetworkRank(n,roads))