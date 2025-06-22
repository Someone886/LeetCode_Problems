# Last updated: 6/22/2025, 2:51:17 PM

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = [] # only projects we can afford
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)

        for i in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -p)
            
            if not max_profit:
                break
            w += -heapq.heappop(max_profit)
        return w

'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = w

        p_c = []
        p_c = [(c, -p) for c, p in zip(capital, profits)]
        
        heapq.heapify(p_c)
        doable = []
        heapq.heapify(doable)
        done = 0

        while p_c and done < k:
            while p_c and p_c[0][0] <= ans:
                next_capital, next_profit = heapq.heappop(p_c)
                heapq.heappush(doable, next_profit)

            if not doable:
                return ans
            else:
                best_profit = heapq.heappop(doable)
                ans -= best_profit
                done += 1
        
        while doable and done < k:
            best_profit = heapq.heappop(doable)
            ans -= best_profit
            done += 1
        
        return ans
'''