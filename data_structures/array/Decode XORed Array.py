class Solution:
    def decode(self, encoded, first):
        arr=[first]
        for val in encoded:
            arr.append(val^arr[-1])
        return arr
s=Solution()
arr=[6,2,7,3]
first=4
print(s.decode(arr,first))