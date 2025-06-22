# Last updated: 6/22/2025, 2:52:11 PM
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        
        return heap[0]