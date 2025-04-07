# Last updated: 4/7/2025, 4:43:35 PM
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-1 * stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            stone_1 = heapq.heappop(neg_stones)
            stone_2 = heapq.heappop(neg_stones)

            if stone_1 < stone_2:
                stone_3 = stone_1 - stone_2
                heapq.heappush(neg_stones, stone_3)
        
        if len(neg_stones) == 1:
            return -neg_stones[0]
        
        return 0
