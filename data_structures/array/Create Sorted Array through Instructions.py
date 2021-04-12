class Solution:
    def start(self,arr,val,n):
        start=0
        end=n
        while start<=end:
            mid=(start+end)//2
            if arr[mid]<val:
                start=mid+1
            else:
                end=mid-1
        return start

    def end(self,arr,val,n):
        start=0
        end=n
        i=-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]<val:
                start=mid+1
            elif arr[mid]>val:
                end=mid-1
            else:
                i=mid
                start+=1
        return i

    def createSortedArray(self, instructions):
        arr=[]
        ans=0
        arr.append(instructions[0])
        for val in instructions[1:]:
            if arr[-1]<=val:
                arr.append(val)
            elif arr[0]>=val:
                arr.insert(0,val)
            else:
                n=len(arr)
                start=self.start(arr,val,n-1)
                arr.insert(start,val)
                end=start
                if arr[start]==arr[end+1]:
                    while arr[end]==arr[start]:
                        end+=1
                # end=self.end(arr,val,n)
                # print(end)
                ans+=min(start,len(arr)-end-1)
        return ans



s=Solution()
arr=[1,5,6,2]
print(s.createSortedArray(arr))