class Solution:
    def maximumTime(self, time: str):

        l=5
        for i in range(l):
            if time[i]=='?':
                if i==0:
                    if time[i+1]!='?':
                        if time[i+1]<'4':
                            time="2"+time[1+i:]
                        else:
                            time = "1" + time[1 + i:]
                    else:
                        time = "2" + time[1 + i:]
                if i==1:
                    if time[i-1]=='2':
                        time=time[:i]+'3'+time[i+1:]
                    else:
                        time = time[:i] + '9' + time[i + 1:]
                if i==3:
                    time = time[:i] + '5' + time[i + 1:]
                if i == 4:
                    time = time[:i] + '9' + time[i + 1:]
            print(time)
        return time

s=Solution()
time = "??:??"
print(s.maximumTime(time))


