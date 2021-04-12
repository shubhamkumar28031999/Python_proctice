class Solution:
    def lengthOfLongestSubstring(self, arr):
        max_length=0
        l=len(arr)
        if l>1:
            for i in range(l-1):
                s=set()
                temp_index=i
                while temp_index<l and arr[temp_index] not in s:
                    s.add(arr[temp_index])
                    temp_index+=1
                max_length=max(max_length,len(s))
        if l==0:
            pass
        if l==1:
            max_length=1
        return max_length

if __name__=="__main__":
    arr= "pwwkew"
    s=Solution().lengthOfLongestSubstring(arr)
    print(s)
