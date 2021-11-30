from collections import deque
class Solution:
    def checkValidString(self, s: str):
        stack1=deque()
        stack2=deque()
        for i in range(len(s)):
            if s[i]=="(":
                stack1.append(i)
            elif s[i]==")":
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
            else:
                stack2.append(i)
        while stack2 and stack1:
            if stack1[-1]<stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False
        if stack1:
            return False
        return True
        

s ="(((((()*)(*)*))())())(()())())))((**)))))(()())()"
print(Solution().checkValidString(s))