# Last updated: 1/3/2026, 4:20:20 PM
1class UnionFind:
2    def __init__(self, n):
3        # Initialize each node as its own parent (n separate components)
4        self.parents = [i for i in range(n)]
5        # Tracks the number of nodes in each component for balancing trees
6        self.size = [1] * n
7    
8    def find(self, node):
9        # Iteratively traverse up the tree to find the root
10        while self.parents[node] != node:
11            # Path Halving optimization: Points node to its grandparent
12            # This flattens the structure to keep find operations near O(1)
13            self.parents[node] = self.parents[self.parents[node]]
14            node = self.parents[node]
15        return self.parents[node]
16    
17    def union(self, node_1, node_2):
18        # Identify the ultimate roots of both nodes
19        parent_1 = self.find(node_1)
20        parent_2 = self.find(node_2)
21
22        # If they already share a root, they are in the same component
23        if parent_1 == parent_2:
24            return False
25        
26        # Union by Size: Attach the smaller component to the larger one
27        # This prevents the tree from becoming too deep/tall
28        if self.size[parent_1] > self.size[parent_2]:
29            self.parents[parent_2] = parent_1
30            self.size[parent_1] += self.size[parent_2]
31        else:
32            self.parents[parent_1] = parent_2
33            self.size[parent_2] += self.size[parent_1]
34        
35        # Return True to indicate a merge actually occurred
36        return True
37
38
39
40class Solution:
41    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
42        # 1. Establish connectivity using Union-Find
43        uf = UnionFind(n)
44        for u, v, w in edges:
45            uf.union(u, v)
46        
47        # 2. Calculate the bitwise AND cost for every component
48        # In this problem, the minimum cost to travel between connected nodes 
49        # is the AND result of all edges in that component because you can 
50        # visit every edge multiple times to reduce the bitwise value.
51        component_cost = {}
52        for u, v, w in edges:
53            root = uf.find(u)
54            if root not in component_cost:
55                # First time seeing this component, start with current edge weight
56                component_cost[root] = w
57            else:
58                # Accumulate the bitwise AND across all edges in the component
59                component_cost[root] &= w
60        
61        # 3. Process each query
62        res = []
63        for u, v in query:
64            root_1 = uf.find(u)
65            root_2 = uf.find(v)
66            
67            # Logic: If nodes share a root, they are connected. 
68            # The cost is the component's AND sum. Otherwise, return -1.
69            cost = -1 if root_1 != root_2 else component_cost[root_1]
70            res.append(cost)
71        
72        return res