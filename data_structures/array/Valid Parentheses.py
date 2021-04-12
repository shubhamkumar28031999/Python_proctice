from collections import deque
class Solution:
    def isValid(self, s: str):
        stack=deque()
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                elif (stack[-1]=='(' and s[i]==')') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='{' and s[i]=='}'):
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False





s=Solution()
d = "([)]"
print(s.isValid(d))