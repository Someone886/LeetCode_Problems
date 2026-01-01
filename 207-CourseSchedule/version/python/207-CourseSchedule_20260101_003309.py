# Last updated: 1/1/2026, 12:33:09 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        # Create an adjacency list where each course points to its prerequisites
4        pre_courses = {}
5        for post, pre in prerequisites:
6            if post not in pre_courses:
7                pre_courses[post] = []
8            pre_courses[post].append(pre)
9
10        # Map to track the state of each course:
11        # False -> Currently visiting (in recursion stack)
12        # True  -> Fully processed (safe, no cycles found from here)
13        if_visited = {}
14
15        def dfs(course):
16            # If already visited, return the stored result (cycle detection or safety)
17            if course in if_visited:
18                return if_visited[course]
19            
20            # Mark the course as "Currently Visiting"
21            if_visited[course] = False
22
23            # Recursively visit all prerequisites
24            if course in pre_courses:
25                for pre in pre_courses[course]:
26                    # If any prerequisite leads back to a course in the current stack, return False
27                    if not dfs(pre):
28                        return False
29            
30            # Mark the course as "Fully Processed/Safe"
31            if_visited[course] = True
32            return True
33
34        # Check every course (handles disconnected components in the graph)
35        for i in range(numCourses):
36            if not dfs(i):
37                return False
38        
39        return True