# Last updated: 1/6/2026, 9:28:11 AM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        # 1. Build the graph
4        graph = {}
5        for u, v, p in flights:
6            if u not in graph: graph[u] = []
7            graph[u].append((v, p))
8        
9        # 2. Priority Queue: (cost, stops, location)
10        # Dijkstra must prioritize 'cost' to ensure the first time we hit 'dst', it's the cheapest.
11        min_q = [(0, 0, src)]
12        
13        # 3. Dictionary to track the best (minimum) stops found for each node
14        # stop_map[node] = min_stops_to_reach_node
15        stop_map = {}
16
17        while min_q:
18            price, stops, node = heapq.heappop(min_q)
19
20            # If we reached the destination, return the price immediately
21            if node == dst:
22                return price
23            
24            # Pruning: 
25            # 1. If we have no more stops allowed, don't explore further.
26            # 2. If we've reached this node before with fewer or equal stops, skip it.
27            if stops > k or stops >= stop_map.get(node, float('inf')):
28                continue
29            
30            # Record the new "best" (fewest) stops for this node
31            stop_map[node] = stops
32            
33            if node in graph:
34                for neighbor, add_price in graph[node]:
35                    if stop_map.get(neighbor, float('inf')) < stops + 1:
36                        continue
37                    heapq.heappush(min_q, (price + add_price, stops + 1, neighbor))
38
39        return -1