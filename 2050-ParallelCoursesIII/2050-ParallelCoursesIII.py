# Last updated: 1/5/2026, 1:32:34 AM
1# Topological sort + min_q (instead of dq for BFS)
2
3class Solution:
4    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
5        # 1. Build the Adjacency List and In-Degree array
6        graph = {}
7        in_degrees = [0] * (n + 1)
8        # Pad 'time' with a dummy value at index 0 because courses are 1-indexed
9        time = [0] + time
10
11        for pre, nxt in relations:
12            if pre not in graph:
13                graph[pre] = []
14            graph[pre].append(nxt)
15            in_degrees[nxt] += 1
16        
17        # 2. Initialize the Min-Heap with all courses that have no prerequisites
18        # The heap stores: (completion_time, course_number)
19        # We use a heap to always process the course that finishes earliest
20        min_q = []
21        for i in range(1, n + 1):
22            if in_degrees[i] == 0:
23                # Initial finish time is just the time to complete the course itself
24                heapq.heappush(min_q, (time[i], i))
25
26        max_time = 0
27
28        # 3. Process the courses in topological order
29        while min_q:
30            # Get the course that finishes soonest
31            finish_time, course_i = heapq.heappop(min_q)
32            
33            # The total time needed is determined by the last course to finish
34            max_time = max(max_time, finish_time)
35
36            # If this course is not a prerequisite for anything else, skip
37            if course_i not in graph:
38                continue
39
40            # Check all courses that depend on this current course (course_i)
41            for neighbor in graph[course_i]:
42                # Decrement in-degree because one prerequisite is now finished
43                in_degrees[neighbor] -= 1
44                
45                # If all prerequisites for the neighbor are done, add to heap
46                if in_degrees[neighbor] == 0:
47                    # Completion time = current finish time + time for the next course
48                    heapq.heappush(min_q, (finish_time + time[neighbor], neighbor))
49        
50        return max_time
51        