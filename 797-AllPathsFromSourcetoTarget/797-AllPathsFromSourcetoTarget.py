# Last updated: 1/3/2026, 7:10:31 PM
1class Solution:
2    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
3        # Initialize an empty list to store all valid paths found
4        res = []
5        
6        # Initialize a double-ended queue for Breadth-First Search (BFS)
7        # Each element in the queue is a tuple: (current_node, path_to_this_node)
8        dq = deque()
9        
10        # Start BFS from node 0 with an empty history path
11        dq.append((0, []))
12        
13        # The target node is always the last node (n - 1)
14        n = len(graph)
15
16        while dq:
17            # Pop the oldest element (FIFO) to explore the graph level by level
18            node, path = dq.popleft()
19            
20            # Create a NEW path including the current node. 
21            # Note: This list concatenation creates a copy, which is necessary
22            # in BFS so that different branches don't overwrite each other.
23            new_path = path + [node]
24            
25            # Check if we have reached the destination node
26            if node == n - 1:
27                # If yes, add this complete path to our final results
28                res.append(new_path)
29                # No need to explore neighbors of the target node
30                continue
31            
32            # Explore all outgoing edges (neighbors) from the current node
33            for neighbor in graph[node]:
34                # Add the neighbor and the current path state to the queue
35                dq.append((neighbor, new_path))
36
37        return res