class Solution:
    def nCr(self, n, r):
        arr=[]
        for i in range(n+1):
            if i==0:
                arr.append(1)
            else:
                arr.append(arr[i-1]*i)

        print(arr)
        return (arr[n]//(arr[n-r]*arr[r]))%((10**9)+7)

c=Solution()
print(c.nCr(10,2))