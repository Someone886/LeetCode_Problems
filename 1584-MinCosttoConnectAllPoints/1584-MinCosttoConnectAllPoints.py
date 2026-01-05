# Last updated: 1/4/2026, 11:03:29 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        n = len(points)
4        
5        # Base case: 0 or 1 point costs nothing to "connect"
6        if n <= 1:
7            return 0
8        
9        # min_heap stores tuples of (distance_to_reach_node, node_index)
10        # We start at index 0 with a cost of 0.
11        min_heap = [(0, 0)]
12        
13        # Track nodes already included in our Minimum Spanning Tree (MST)
14        visited = set()
15        total_dist = 0
16        
17        # We continue until we have connected all n points
18        while len(visited) < n:
19            # Pop the edge with the smallest distance from the heap
20            dist, curr_node = heapq.heappop(min_heap)
21            
22            # If we've already added this node to our MST, skip it
23            if curr_node in visited:
24                continue
25            
26            # 1. Add node to MST
27            visited.add(curr_node)
28            total_dist += dist
29            
30            # 2. Optimization: If all points are visited, stop immediately
31            if len(visited) == n:
32                break
33            
34            # 3. Explore neighbors
35            # Instead of a pre-built graph, we calculate distances to all 
36            # other points on-the-fly to save memory (O(1) space vs O(N^2))
37            x1, y1 = points[curr_node]
38            for next_node in range(n):
39                if next_node not in visited:
40                    x2, y2 = points[next_node]
41                    # Manhattan distance: |x1 - x2| + |y1 - y2|
42                    manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
43                    heapq.heappush(min_heap, (manhattan_dist, next_node))
44        
45        return total_dist
46
47        
48# class Solution:
49#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
50#         n = len(points)
51#         if n <= 1:
52#             return 0
53        
54#         n = len(points)
55
56#         for i in range(n - 1):
57#             x_i, y_i = points[i]
58#             if i not in graph:
59#                 graph[i] = []
60
61#             for j in range(i + 1, n):
62#                 x_j, y_j = points[j]
63#                 if j not in graph:
64#                     graph[j] = []
65
66#                 dist = abs(x_i - x_j) + abs(y_i - y_j)
67                
68#                 graph[i].append((j, dist))
69#                 graph[j].append((i, dist))
70        
71#         min_heap = [(0, 0)]
72#         visited = set()
73#         total_dist = 0
74
75#         while min_heap:
76#             dist, node = heapq.heappop(min_heap)
77
78#             if node in visited:
79#                 continue
80#             else:
81#                 visited.add(node)
82            
83#             total_dist += dist
84
85#             for neighbor, neighbor_dist in graph[node]:
86#                 if neighbor not in visited:
87#                     heapq.heappush(min_heap, (neighbor_dist, neighbor))
88        
89#         return total_dist