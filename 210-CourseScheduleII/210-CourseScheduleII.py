# Last updated: 1/5/2026, 1:26:06 AM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        n = numCourses
4        in_degrees = [0] * n
5        graph = {}
6
7        for nxt, pre in prerequisites:
8            if pre not in graph:
9                graph[pre] = []
10            graph[pre].append(nxt)
11            in_degrees[nxt] += 1
12        
13        dq = deque([i for i in range(n) if in_degrees[i] == 0])
14        cnt = 0
15        ans = []
16
17        while dq:
18            course = dq.popleft()
19            cnt += 1
20            ans.append(course)
21
22            if course in graph:
23                for neighbor in graph[course]:
24                    in_degrees[neighbor] -= 1
25                    if in_degrees[neighbor] == 0:
26                        dq.append(neighbor)
27        
28        return ans if cnt == n else []
29