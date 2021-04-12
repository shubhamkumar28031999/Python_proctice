class RangeModule:

    def __init__(self):
        self.range=[]

    def addRange(self, left, right):
        self.range=[x for x in range(left,right)]

    def queryRange(self, left: int, right: int):
        b=True
        for x in range(left,right):
            if x not in self.range:
                return "false"
        return "true"

    def removeRange(self, left: int, right: int):
        if max(self.range)>=right and min(self.range)<=left:
            for x in range(left,right):
                self.range.remove(x)

if __name__=="__main__":
    obj = RangeModule()
    obj.addRange(10, 20)
    # print(obj.queryRange(14,16))
    obj.removeRange(14, 16)
    print(obj.queryRange(10, 14))
    print(obj.queryRange(13, 15))
    print(obj.queryRange(16, 17))