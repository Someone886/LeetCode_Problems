# Last updated: 1/11/2026, 6:27:13 PM
1from collections import deque, defaultdict
2
3class Solution:
4    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
5        if not root:
6            return []
7        
8        # column_nodes stores {column_index: [(row_index, value), ...]}
9        column_nodes = defaultdict(list)
10        
11        # Track the range of columns to avoid sorting keys at the end
12        min_col = max_col = 0
13        
14        # BFS queue stores (node, row, column)
15        dq = deque([(root, 0, 0)])
16
17        while dq:
18            node, row, col = dq.popleft()
19            
20            # 1. Update the range of columns we've seen
21            min_col = min(min_col, col)
22            max_col = max(max_col, col)
23            
24            # 2. Store row and value for sorting within the same column
25            column_nodes[col].append((row, node.val))
26
27            # 3. Standard BFS exploration
28            if node.left:
29                dq.append((node.left, row + 1, col - 1))
30            if node.right:
31                dq.append((node.right, row + 1, col + 1))
32        
33        res = []
34        
35        # 4. Use the tracked range to iterate through columns in order
36        # This replaces sorted(column_nodes.keys())
37        for col in range(min_col, max_col + 1):
38            
39            # 5. Sort the nodes within this specific column
40            # Tuples are sorted by the first element (row), then the second (val)
41            column_nodes[col].sort()
42            
43            # 6. Extract only the values for the final result
44            res.append([val for row, val in column_nodes[col]])
45            
46        return res
47
48'''
49class Solution:
50    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
51        if not root:
52            return []
53        
54        # Dictionary to store: {column: [(row, value), ...]}
55        column_nodes = defaultdict(list)
56
57        # BFS: Store (node, row, col)
58        dq = deque([(root, 0, 0)])
59
60        while dq:
61            node, row, col = dq.popleft()
62            
63            # Store both row and value to sort correctly later
64            column_nodes[col].append((row, node.val))
65
66            if node.left:
67                dq.append((node.left, row + 1, col - 1))
68            if node.right:
69                dq.append((node.right, row + 1, col + 1))
70        
71        # Sort columns by their horizontal index
72        sorted_cols = sorted(column_nodes.keys())
73        res = []
74        
75        for col in sorted_cols:
76            # Sort by row index first, then by value (Python's sort does this by default for tuples)
77            column_nodes[col].sort()
78            
79            # Extract just the values after sorting
80            res.append([val for row, val in column_nodes[col]])
81        
82        return res
83'''