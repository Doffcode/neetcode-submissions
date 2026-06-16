class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        ret = None
        self.prices.append(price)
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        if not self.stack :
            ret = len(self.prices)
        else:
            ret = len(self.prices) - self.stack[-1] -1
        self.stack.append(len(self.prices)-1)
        return ret

