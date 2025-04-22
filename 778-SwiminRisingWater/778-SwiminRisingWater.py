# Last updated: 4/22/2025, 4:24:15 AM
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
            water, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            max_water = max(water, max_water)

            for dx, dy in dirs:
                if 0 <= x + dx < n and 0 <= y + dy < n and (x + dx, y + dy) not in visited:
                    heapq.heappush(heap, (max(max_water, grid[x + dx][y + dy]), x + dx, y + dy))
        
        return max_water
        