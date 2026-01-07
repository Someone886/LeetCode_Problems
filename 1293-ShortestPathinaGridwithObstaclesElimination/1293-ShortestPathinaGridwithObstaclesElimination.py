# Last updated: 1/7/2026, 12:52:27 PM
1class Solution:
2    def shortestPath(self, grid: List[List[int]], k: int) -> int:
3        n, m = len(grid), len(grid[0])
4        
5        # --- OPTIMIZATION: MANHATTAN DISTANCE ---
6        # The shortest possible path is the Manhattan distance: (n-1) + (m-1).
7        # If we have enough 'k' to break every potential obstacle along that path,
8        # we don't need BFS; we can just return the distance immediately.
9        if k >= (n - 1) + (m - 1):
10            return (n - 1) + (m - 1)
11        
12        # Standard 4-directional movement: Up, Down, Left, Right
13        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
14        
15        # --- STATE TRACKING ---
16        # seen stores {(row, col): min_obstacles_used_to_reach_here}
17        # This is the "secret sauce." We only revisit a cell if we reach it 
18        # with FEWER obstacles destroyed than our previous visit.
19        seen = {(0, 0): 0}
20
21        # Queue stores (row, col, obstacles_destroyed)
22        dq = deque([(0, 0, 0)])
23        steps = 0
24
25        while dq:
26            # Process the current "layer" of BFS to track steps accurately
27            for _ in range(len(dq)):
28                r, c, o = dq.popleft()
29
30                # Goal reached: BFS guarantees this is the shortest path
31                if (r, c) == (n - 1, m - 1):
32                    return steps
33                
34                if (r, c) in seen and o > seen[(r, c)]:
35                    continue
36
37                for dr, dc in directions:
38                    nr, nc = r + dr, c + dc
39                    
40                    # Boundary check
41                    if 0 <= nr < n and 0 <= nc < m:
42                        # Calculate obstacles used if we move to this neighbor
43                        new_o = o + grid[nr][nc]
44                        
45                        # --- PRUNING LOGIC ---
46                        # 1. We must have enough k remaining (new_o <= k)
47                        # 2. We only move there if this path is "better" (uses fewer k)
48                        #     than any previous path to this specific (nr, nc)
49                        if new_o <= k and new_o < seen.get((nr, nc), float('inf')):
50                            seen[(nr, nc)] = new_o
51                            dq.append((nr, nc, new_o))
52            
53            # Increment steps after exploring all nodes at the current distance
54            steps += 1
55        
56        # If the queue empties without reaching the target
57        return -1