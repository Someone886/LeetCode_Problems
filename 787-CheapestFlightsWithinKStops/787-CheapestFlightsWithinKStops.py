# Last updated: 1/6/2026, 9:47:38 AM
1# Problem	         Primary Priority (The "Money")	The Constraint (The "Resource")
2# Cheapest Flights	  Cumulative Price (Edge Sum)	  Cumulative Stops (Node Count)
3# Min Cost	          Cumulative Fees (Node Sum)	  Cumulative Time (Edge Sum)
4
5class Solution:
6    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
7        # 1. Build the graph
8        graph = {}
9        for u, v, p in flights:
10            if u not in graph: graph[u] = []
11            graph[u].append((v, p))
12        
13        # 2. Priority Queue: (cost, stops, location)
14        # Dijkstra must prioritize 'cost' to ensure the first time we hit 'dst', it's the cheapest.
15        min_q = [(0, 0, src)]
16        
17        # 3. Dictionary to track the best (minimum) stops found for each node
18        # stop_map[node] = min_stops_to_reach_node
19        stop_map = {}
20
21        while min_q:
22            price, stops, node = heapq.heappop(min_q)
23
24            # If we reached the destination, return the price immediately
25            if node == dst:
26                return price
27            
28            # Pruning: 
29            # 1. If we have no more stops allowed, don't explore further.
30            # 2. If we've reached this node before with fewer or equal stops, skip it.
31            if stops > k or stops >= stop_map.get(node, float('inf')):
32                continue
33            
34            # Record the new "best" (fewest) stops for this node
35            stop_map[node] = stops
36            
37            if node in graph:
38                for neighbor, add_price in graph[node]:
39                    if stop_map.get(neighbor, float('inf')) < stops + 1:
40                        continue
41                    heapq.heappush(min_q, (price + add_price, stops + 1, neighbor))
42
43        return -1