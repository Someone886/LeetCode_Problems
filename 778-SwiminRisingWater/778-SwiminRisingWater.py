# Last updated: 4/22/2025, 5:15:37 AM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # heap point = grid[x][y], x, y
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)
        visited = set()
        max_water = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while (n - 1, n - 1) not in visited:
            max_water, x, y = heapq.heappop(heap)
            
            if x == y == n - 1:
                return max_water

            if (x, y) in visited:
                continue
            else:
                visited.add((x, y))

            for dx, dy in dirs:
                if 0 <= x + dx < n and 0 <= y + dy < n and (x + dx, y + dy) not in visited:
                    heapq.heappush(heap, (max(max_water, grid[x + dx][y + dy]), x + dx, y + dy))
        
        return max_water

'''
issue with DFS + DP:
19 20
7  6
Suppose we are at 7, we mark 7 as visited and explore 19 and 6 as the next node. 
Now we are at 19, the only path to get to 6 is 19 -> 20 -> 6, marking node 19 with max cost = 20.
However, at 19, the correct path is 19 -> 7 -> 6 with max cost = 19.
But since we already marked 7, we blocked the revisiting of 7 from 19.
'''
