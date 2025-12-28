# Last updated: 12/28/2025, 12:26:43 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rotton_locations = deque()
4        good_orange_cnt = 0
5        visited = set()
6        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
7
8        for r in range(len(grid)):
9            for c in range(len(grid[0])):
10                if grid[r][c] == 2:
11                    rotton_locations.append((r, c))
12                    visited.add((r, c))
13                elif grid[r][c] == 1:
14                    good_orange_cnt += 1
15        
16        if good_orange_cnt == 0:
17            return 0
18        
19        time = -1
20        while rotton_locations:
21            for i in range(len(rotton_locations)):
22                rotton_location_r, rotton_location_c = rotton_locations.popleft()
23
24                for dx, dy in directions:
25                    neighbor_r, neighbor_c = rotton_location_r + dx, rotton_location_c + dy
26                    if 0 <= neighbor_r < len(grid) and \
27                        0 <= neighbor_c < len(grid[0]) and \
28                        (neighbor_r, neighbor_c) not in visited and \
29                        grid[neighbor_r][neighbor_c] == 1:
30                            rotton_locations.append((neighbor_r, neighbor_c))
31                            visited.add((neighbor_r, neighbor_c))
32                            good_orange_cnt -= 1
33            
34            time += 1
35        
36        return time if good_orange_cnt == 0 else -1
37