# Last updated: 1/3/2026, 11:25:21 AM
1import heapq
2
3class Solution:
4    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
5        # 1. Build the Graph
6        # We use a dictionary where the key is the source node 'u'
7        # and the value is a list of tuples (neighbor, weight).
8        graph = {}
9        for time in times:
10            u, v, t = time
11            if u not in graph:
12                graph[u] = []
13            graph[u].append((v, t))
14
15        # 2. Initialize State Variables
16        # max_time: Tracks the time it takes for the signal to reach the last node.
17        # min_queue: A priority queue (min-heap) to always process the node with 
18        # the smallest cumulative time first.
19        # visited: A set to keep track of nodes that have reached their minimum travel time.
20        max_time = 0
21        min_queue = []
22        visited = set()
23
24        # 3. Start Dijkstra's from the source node 'k'
25        # Format: (total_time_from_source, current_node)
26        heapq.heappush(min_queue, (0, k))
27
28        while min_queue:
29            # Pop the node with the smallest travel time.
30            time, node = heapq.heappop(min_queue)
31            
32            # If the node has already been visited, skip it.
33            # In Dijkstra's, the first time we pop a node, we've found its 
34            # shortest path from the source.
35            if node in visited:
36                continue
37            else:
38                visited.add(node)
39
40            # Update the maximum time. Since we pop nodes in increasing 
41            # order of time, the last node we visit will determine the result.
42            max_time = max(time, max_time)
43
44            # Safety check: if the node has no outgoing edges, skip to next iteration.
45            if node not in graph:
46                continue 
47
48            # 4. Explore Neighbors
49            # For each neighbor of the current node, calculate the time to reach it.
50            for neighbor_node, edge_weight in graph[node]:
51                if neighbor_node not in visited:
52                    # Push the cumulative time and the neighbor to the priority queue.
53                    # Corrected syntax: added min_queue as the destination list.
54                    heapq.heappush(min_queue, (edge_weight + time, neighbor_node))
55        
56        # 5. Final Result
57        # If the number of visited nodes equals n, return the max_time.
58        # Otherwise, some nodes were unreachable, so return -1.
59        return max_time if len(visited) == n else -1