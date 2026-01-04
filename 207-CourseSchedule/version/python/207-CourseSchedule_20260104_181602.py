# Last updated: 1/4/2026, 6:16:02 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        adj = [[] for _ in range(numCourses)]
4        in_degree = [0] * numCourses
5        
6        # Build the graph
7        for course, pre in prerequisites:
8            adj[pre].append(course)
9            in_degree[course] += 1
10            
11        # 1. Start with courses that have 0 prerequisites
12        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
13        
14        visited_count = 0
15        while queue:
16            curr = queue.popleft()
17            visited_count += 1
18            
19            # 2. "Take" the course and reduce in-degree of neighbors
20            for neighbor in adj[curr]:
21                in_degree[neighbor] -= 1
22                # 3. If neighbor has no more prerequisites, add to queue
23                if in_degree[neighbor] == 0:
24                    queue.append(neighbor)
25        
26        # If we couldn't visit all courses, there's a cycle
27        return visited_count == numCourses
28
29# class Solution:
30#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
31#         # Create an adjacency list where each course points to its prerequisites
32#         pre_courses = {}
33#         for post, pre in prerequisites:
34#             if post not in pre_courses:
35#                 pre_courses[post] = []
36#             pre_courses[post].append(pre)
37
38#         # Map to track the state of each course:
39#         # False -> Currently visiting (in recursion stack)
40#         # True  -> Fully processed (safe, no cycles found from here)
41#         if_visited = {}
42
43#         def dfs(course):
44#             # If already visited, return the stored result (cycle detection or safety)
45#             if course in if_visited:
46#                 return if_visited[course]
47            
48#             # Mark the course as "Currently Visiting"
49#             if_visited[course] = False
50
51#             # Recursively visit all prerequisites
52#             if course in pre_courses:
53#                 for pre in pre_courses[course]:
54#                     # If any prerequisite leads back to a course in the current stack, return False
55#                     if not dfs(pre):
56#                         return False
57            
58#             # Mark the course as "Fully Processed/Safe"
59#             if_visited[course] = True
60#             return True
61
62#         # Check every course (handles disconnected components in the graph)
63#         for i in range(numCourses):
64#             if not dfs(i):
65#                 return False
66        
67#         return True