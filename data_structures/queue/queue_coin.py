import sys
from collections import deque
class temp_class:
    def __init__(self):
        self.max_size=-sys.maxsize
    def subset_sum(self,numbers, target, partial=[]):
        s = sum(partial)
        if s == target:
            self.max_size=max(self.max_size,len(partial))
        if s >= target:
            return
        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            self.subset_sum(remaining, target, partial + [n])

    def max_len(self,arr,totsl):
        self.subset_sum(arr,totsl)
        return self.max_size

class Solution:
    def __init__(self):
        self.queue = deque()
    def solve(self,arr):
        result=[]
        for val in arr:
            if val[0]==1:
                self.queue.appendleft(val[1])
            elif val[0]==2:
                self.queue.pop()
            else:
                temp=temp_class()
                result.append(temp.max_len(list(self.queue),val[1]))
        return result




s=Solution()

arr = [
    [1,1],
    [1,2],
    [1,2],
    [1,3],
    [3,4],
    [3,5]
]
n=5
print(s.solve(arr))