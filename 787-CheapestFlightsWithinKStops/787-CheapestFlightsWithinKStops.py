# Last updated: 4/22/2025, 6:44:27 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford algorithm that can intuitively handle the k stops condition.
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            # modify new_prices 
            # so that only destinations within i stops from src (which are reachable) are updated
            new_prices = prices.copy()

            for start, end, price in flights:
                if prices[start] + price < new_prices[end]:
                    new_prices[end] = prices[start] + price

            prices = new_prices
        
        return -1 if prices[dst] == float("inf") else prices[dst]