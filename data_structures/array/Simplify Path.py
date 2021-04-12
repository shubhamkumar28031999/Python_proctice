from collections import deque
class Solution:
    def simplifyPath(self, path):
        path = list(filter(lambda a: a != "" and a!='.', path.split("/")))
        print(path)
        stack = deque()
        for i in path:
            if i == '..':
                if len(stack)>=1:
                    stack.pop()
            else:
                stack.append(i)
        final_str='/'
        for val in stack:
            final_str+=val+'/'
        if len(final_str)==1:
            return final_str
        else:
            return final_str[:-1]
s = Solution()
l ="/a/./b/../../c/"
print(s.simplifyPath(l))
