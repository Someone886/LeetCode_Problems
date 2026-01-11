# Last updated: 1/11/2026, 6:02:00 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        if not self.stack:
8            self.stack.append([price, 1])
9            return 1
10        
11        curr_lasting_days = 1
12        while self.stack and price >= self.stack[-1][0]:
13            prev_price, prev_lasting_days = self.stack.pop()
14            curr_lasting_days += prev_lasting_days
15        
16        self.stack.append([price, curr_lasting_days])
17        return curr_lasting_days
18
19
20# Your StockSpanner object will be instantiated and called as such:
21# obj = StockSpanner()
22# param_1 = obj.next(price)