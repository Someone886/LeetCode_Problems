# Last updated: 4/22/2025, 7:07:27 PM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        heap = [(0, 0)]
        heapq.heapify(heap)
        visited = set()

        # prim's algo
        # compute the dist between two points on the run
        # add a point's neighbor to the heap if not visited
        # if all points visitied, break out and return
        
        while len(visited) < len(points):
            dist, pt = heapq.heappop(heap)
            if pt in visited:
                continue
            
            visited.add(pt)
            total += dist
            x, y = points[pt][0], points[pt][1]

            for i in range(len(points)):
                if i in visited:
                    continue
                
                x_j, y_j = points[i][0], points[i][1]
                next_dist = abs(x - x_j) + abs(y - y_j)
                heapq.heappush(heap, (next_dist, i))
        
        return total