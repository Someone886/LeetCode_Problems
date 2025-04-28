# Last updated: 4/28/2025, 1:35:49 AM
class StockSpanner:

    def __init__(self):
        self.stock_stack = []
        self.span = []

    def next(self, price: int) -> int:
        if not self.stock_stack:
            self.stock_stack.append(price)
            self.span.append(1)
            return 1
        else:
            total_span = 1
            
            while self.stock_stack and self.stock_stack[-1] <= price:
                last_price = self.stock_stack.pop()
                last_span = self.span.pop()
                total_span += last_span
            
            self.stock_stack.append(price)
            self.span.append(total_span)

            return total_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)