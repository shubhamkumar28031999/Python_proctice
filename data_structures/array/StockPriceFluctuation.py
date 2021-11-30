import math
class StockPrice:
    def __init__(self):
        self.Stock={}
        self.max=0
        self.min=2**31
        self.last=-1

    def update(self, timestamp, price) -> None:
        if timestamp not in self.Stock:
            self.Stock[timestamp]=price
            self.max=max(self.max,price)
            self.min=min(self.min,price)
            self.last=price
        else:
            timestamp=max(self.Stock.keys())+1
            self.Stock[timestamp]=price
            self.max=max(self.max,price)
            self.min=min(self.min,price)
            self.last=price
        print(self.Stock)

    def current(self) -> int:
        return self.last

    def maximum(self) -> int:
        return self.max

    def minimum(self) -> int:
        if self.min == 2**32:
            return 0
        return 0

stockPrice = StockPrice()
stockPrice.update(1, 10)
stockPrice.update(2, 5)  
print(stockPrice.current())   
print(stockPrice.maximum())
stockPrice.update(1, 3)            
print(stockPrice.maximum())     
stockPrice.update(4, 2)  
print(stockPrice.minimum())  