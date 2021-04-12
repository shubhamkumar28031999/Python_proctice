import math as mt
import sys
class Solution:
    def Prime(self,upper):
        arr=[]
        for num in range(2, upper + 1):
            if num > 0:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    arr.append(num)
        return arr

    def max_count(self,val,all_primes):
        max_count=0
        number=-sys.maxsize
        count=0
        for prime in all_primes:
            if prime>val:
                break
            else:
                if val%prime==0:
                    count+=1
        return count



    def solve(self,A,B):
        sum = 0
        m=max(A)
        d={}
        all_primes=self.Prime(m)
        for val in A:
            d[val]=self.max_count(val,all_primes)
        print(d)
        for i in range(0,len(A)-B+1):
            count = 0
            for val in A[i:i+B]:
                if d[val]>count:
                    count=d[val]
                    s=val
            # print(s)
            sum+=s
        return sum%((10**9)+7)

# A=[10,2,1,1,2]
# A=[18,36,15,210]
A=[477,788,70,819,229,368,572,297,883,392]
B=4
s=Solution()
print(s.solve(A,B))