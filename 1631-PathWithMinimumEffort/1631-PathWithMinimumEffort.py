# Last updated: 11/7/2025, 11:04:09 PM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_eff = 0
        visited = set()
        n = len(heights)
        m = len(heights[0])

        # min effort to reach an index, r, c
        q = [(0, 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while (n-1, m-1) not in visited:
            eff, r, c = heapq.heappop(q)
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            min_eff = eff

            for (dr, dc) in directions:
                if 0 <= r + dr < n and 0 <= c + dc < m:
                    if (r + dr, c + dc) not in visited:
                        neighbor_height = heights[r + dr][c + dc]
                        heapq.heappush(q, (max(min_eff, abs(neighbor_height - heights[r][c])), r + dr, c + dc))
        
        return min_eff