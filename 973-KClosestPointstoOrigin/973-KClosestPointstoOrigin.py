# Last updated: 4/7/2025, 6:37:55 PM
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        order = 0

        for point in points:
            x, y = point[0], point[1]
            sq_distance = x**2 + y**2

            heapq.heappush(heap, (-sq_distance, order, point))
            order += 1

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [tup[2] for tup in heap]