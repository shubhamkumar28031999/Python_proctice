class Solution:
    def minOperations(self, grid, x) -> int:
        A=[]
        for
        cost = 0
        A.sort();
        K = A[int(n / 2)]
        for i in range(0, n):
            cost = cost + abs(A[i] - K)
        if n % 2 == 0:
            tempCost = 0
            K = A[int(n / 2) - 1]
            for i in range(0, n):
                tempCost = tempCost + abs(A[i] - K)
            cost = min(cost, tempCost)
        return cost