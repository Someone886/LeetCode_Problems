# Last updated: 1/5/2026, 1:35:52 AM
1# BFS
2
3class Solution:
4    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
5        # 1. Build the Adjacency List and In-Degree Array
6        # Using a list of lists is more memory-efficient than a dictionary for dense graphs.
7        graph = [[] for _ in range(n + 1)]
8        in_degrees = [0] * (n + 1)
9        
10        for pre, nxt in relations:
11            graph[pre].append(nxt)
12            in_degrees[nxt] += 1
13        
14        # 2. dist[i] stores the EARLIEST possible time course 'i' can finish.
15        # We initialize it with 0s. 
16        dist = [0] * (n + 1)
17        queue = deque()
18        
19        # 3. Initialize the Queue with courses that have no prerequisites
20        for i in range(1, n + 1):
21            if in_degrees[i] == 0:
22                queue.append(i)
23                # If a course has no prerequisites, its finish time is just its own duration.
24                # Note: 'time' array is 0-indexed, so we use time[i-1].
25                dist[i] = time[i-1]
26        
27        # 4. Standard BFS (Kahn's Algorithm)
28        while queue:
29            curr = queue.popleft()
30            
31            # Explore courses that depend on the current finished course
32            for neighbor in graph[curr]:
33                # THE CORE LOGIC:
34                # The earliest a 'neighbor' can finish is its own time PLUS 
35                # the maximum finish time of all its prerequisites.
36                # We use max() because we must wait for the slowest prerequisite to finish.
37                dist[neighbor] = max(dist[neighbor], dist[curr] + time[neighbor-1])
38                
39                # Standard topological sort: decrease in-degree
40                in_degrees[neighbor] -= 1
41                
42                # If all prerequisites for this neighbor are now processed
43                if in_degrees[neighbor] == 0:
44                    queue.append(neighbor)
45        
46        # 5. The total time to finish everything is the maximum finish time found in 'dist'
47        return max(dist)
48
49
50# # Topological sort + min_q (instead of dq for BFS)
51
52# class Solution:
53#     def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
54#         # 1. Build the Adjacency List and In-Degree array
55#         graph = {}
56#         in_degrees = [0] * (n + 1)
57#         # Pad 'time' with a dummy value at index 0 because courses are 1-indexed
58#         time = [0] + time
59
60#         for pre, nxt in relations:
61#             if pre not in graph:
62#                 graph[pre] = []
63#             graph[pre].append(nxt)
64#             in_degrees[nxt] += 1
65        
66#         # 2. Initialize the Min-Heap with all courses that have no prerequisites
67#         # The heap stores: (completion_time, course_number)
68#         # We use a heap to always process the course that finishes earliest
69#         min_q = []
70#         for i in range(1, n + 1):
71#             if in_degrees[i] == 0:
72#                 # Initial finish time is just the time to complete the course itself
73#                 heapq.heappush(min_q, (time[i], i))
74
75#         max_time = 0
76
77#         # 3. Process the courses in topological order
78#         while min_q:
79#             # Get the course that finishes soonest
80#             finish_time, course_i = heapq.heappop(min_q)
81            
82#             # The total time needed is determined by the last course to finish
83#             max_time = max(max_time, finish_time)
84
85#             # If this course is not a prerequisite for anything else, skip
86#             if course_i not in graph:
87#                 continue
88
89#             # Check all courses that depend on this current course (course_i)
90#             for neighbor in graph[course_i]:
91#                 # Decrement in-degree because one prerequisite is now finished
92#                 in_degrees[neighbor] -= 1
93                
94#                 # If all prerequisites for the neighbor are done, add to heap
95#                 if in_degrees[neighbor] == 0:
96#                     # Completion time = current finish time + time for the next course
97#                     heapq.heappush(min_q, (finish_time + time[neighbor], neighbor))
98        
99#         return max_time
100        