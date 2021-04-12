class Solution:
    def canFormArray(self, arr, pieces):
        l=len(arr)
        i=0
        ls=[]
        while i<l:
            flag = 0
            for val in pieces:
                if val[0] == arr[i]:
                    ls+=val
                    i+=len(val)
                    flag=1
                    pieces.remove(val)
                    break
            if flag==0:
                return False
        if arr!=ls:
            return False
        return True

arr = [49,18,16]
pieces = [[16,18,49]]
s=Solution()
print(s.canFormArray(arr,pieces))


