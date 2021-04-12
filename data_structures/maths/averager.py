class Avrager:
    def __init__(self):
        self.data=[]
    def add(self,val):
        self.data.append(val)
    def __call__(self):
        return sum(self.data)/len(self.data)


a=Avrager()
a.add(10)
a.add(30)
print(a())