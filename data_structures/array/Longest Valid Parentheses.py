from collections import deque
class Solution:
    def longestValidParentheses(self, s):
        l=len(s)
        i=0
        longest_parna=0
        queue=deque()
        temp=0
        while i<l:
            if s[i]=="(":
                queue.append("(")
                temp+=1
                longest_parna=max(longest_parna,temp)
            else:
                if len(queue)>0:
                    queue.pop()
                    temp+=1
                    longest_parna = max(longest_parna, temp)
                else:
                    queue.clear()
                    temp=0
            i+=1
        return longest_parna-len(queue)

s=Solution()
a ="()(()"
print(s.longestValidParentheses(a))

