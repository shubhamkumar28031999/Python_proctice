class Solution:
    def exclusiveTime(self, n, logs):
        stack,prev=[],0
        result=[0]*n
        for val in logs:
            temp=val.split(":")
            if temp[1]=="start":
                if stack:
                    result[stack[-1]]+=int(temp[2])-prev
                stack.append(int(temp[0]))
                prev=int(temp[2])
            else:
                result[stack.pop()]+=int(temp[2])-prev+1
                prev=int(temp[2])+1
        return result
                
        

            


n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
s=Solution()
print(s.exclusiveTime(n,logs))