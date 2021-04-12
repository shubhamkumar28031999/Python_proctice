class RecentCounter:
    def __init__(self):
        self.lst = []
        self.counter = 0

    def ping(self, t):
        self.lst.append(t)
        self.counter += 1
        i = self.counter-1
        count=0
        while i>=0 and self.lst[i] >= t - 3000:
            count+=1
            i-=1
        return count


obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
