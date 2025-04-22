# Last updated: 4/22/2025, 6:39:28 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford algorithm that can intuitively handle the k stops condition.
        cost_cnt = [{} for _ in range(n)]
        cost_cnt[src][-1] = 0

        for _ in range(n - 1):
            for start, end, price in flights:
                if not cost_cnt[start]:
                    continue
                
                start_cost_cnt = cost_cnt[start]
                for stop_cnt, cost in start_cost_cnt.items():
                    new_stop_cnt = stop_cnt + 1
                    new_cost = cost + price
                    
                    if new_stop_cnt <= k:
                        if new_stop_cnt not in cost_cnt[end]:
                            cost_cnt[end][new_stop_cnt] = new_cost
                        elif new_cost < cost_cnt[end][new_stop_cnt]:
                            cost_cnt[end][new_stop_cnt] = new_cost
        
        if not cost_cnt[dst]:
            return -1
        
        min_cost = min(cost_cnt[dst].values())
        if min_cost != float('inf'):
            return min_cost
        else:
            return -1