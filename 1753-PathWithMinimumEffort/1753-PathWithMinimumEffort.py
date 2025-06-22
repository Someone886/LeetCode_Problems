# Last updated: 6/22/2025, 2:50:41 PM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minHeap = [(0, 0, 0)] 
        visited = set()
        
        while minHeap:
            effort, x, y = heappop(minHeap)

            if (x, y) in visited:
                continue
            else:
                visited.add((x,y))

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    heappush(minHeap, (new_effort, nx, ny))
        