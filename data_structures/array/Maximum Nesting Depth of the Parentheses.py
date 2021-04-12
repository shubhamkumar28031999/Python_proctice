from collections import  deque
class Solution:
    def maxDepth(self, s):
        stack=deque()
        l=len(s)
        max_length=0
        for i in range(l):
            if s[i]=='(' or s[i]==')':
                if s[i]=='(':
                    stack.append('(')
                    max_length=max(max_length,len(stack))
                else:
                    stack.pop()
        return max_length

if __name__=="__main__":
    print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))
