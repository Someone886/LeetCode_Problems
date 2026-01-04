# Last updated: 1/4/2026, 5:36:18 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        # At first, each node's parent is itself
4        parents = [i for i in range(len(edges) + 1)]
5
6        # Put the subtree with less nodes to the subtree with more nodes to form a larger subtree
7        node_cnts = [1] * (len(edges) + 1)
8        
9        # To make the tree flat
10        def find(n): 
11            parent = parents[n]
12            # 1. while n -> parent -> parents[parent]
13            # 2. then make parent and parents[parent] the same level: 
14            #    n -> parent (sibling with) parents[parent] -> parents[parents[parent]]
15            # 3. move 1 level up: parent now points to parents[parent]
16            # 4. n -> root parent (another node or itself), and return root parent
17
18            while parent != parents[parent]: # 1
19                parents[parent] = parents[parents[parent]] # 2
20                parent = parents[parent] # 3
21            
22            # parents[n] = parent
23
24            return parent # 4
25        
26        def union(n1, n2):
27            parent_1, parent_2 = find(n1), find(n2)
28            
29            # If two nodes point to the same root, then a cycle forms.
30            if parent_1 == parent_2:
31                return False
32            
33            # parent with less node cnt -> parent with more node cnt
34            # then update node cnt in the bigger subtree
35            if node_cnts[parent_1] > node_cnts[parent_2]:
36                parents[parent_2] = parent_1
37                node_cnts[parent_1] += node_cnts[parent_2]
38            
39            else:
40                parents[parent_1] = parent_2
41                node_cnts[parent_2] += node_cnts[parent_1]
42
43            return True
44        
45        for n1, n2 in edges:
46            # If n1 and n2 are not able to be unioned, then they have the same parent -> cycle
47            if not union(n1, n2):
48                return [n1, n2]