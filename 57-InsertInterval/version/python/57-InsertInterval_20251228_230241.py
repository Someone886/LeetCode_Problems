# Last updated: 12/28/2025, 11:02:41 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        ans = []
4        i = 0
5        n = len(intervals)
6        new_start, new_end = newInterval
7
8        # 1. Add all intervals that come strictly BEFORE the new interval
9        while i < n and intervals[i][1] < new_start:
10            ans.append(intervals[i])
11            i += 1
12
13        # 2. Merge all overlapping intervals
14        # An overlap exists if the current interval starts before or at new_end
15        while i < n and intervals[i][0] <= new_end:
16            new_start = min(new_start, intervals[i][0])
17            new_end = max(new_end, intervals[i][1])
18            i += 1
19        
20        # Add the final merged interval
21        ans.append([new_start, new_end])
22
23        # 3. Add all remaining intervals that come strictly AFTER
24        ans.extend(intervals[i:])
25
26        return ans
27
28
29# class Solution:
30#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
31#         ans = []
32#         new_start, new_end = newInterval
33#         inserted = False
34        
35
36#         for i in range(len(intervals)):
37#             start_i, end_i = intervals[i]
38
39#             if end_i < new_start:
40#                 ans.append(intervals[i])
41#                 continue
42            
43#             merged_start = min(start_i, new_start)
44#             j = i
45
46#             while j < len(intervals) and intervals[j][1] <= new_end:
47#                 j += 1
48
49#             if j == len(intervals):
50#                 merged_end = new_end
51#                 ans.append([merged_start, merged_end])
52#                 inserted = True
53#             elif new_end >= intervals[j][0]:
54#                 merged_end = intervals[j][1]
55#                 ans.append([merged_start, merged_end])
56#                 inserted = True
57#                 ans.extend(intervals[j + 1:])
58#             else:
59#                 merged_end = new_end
60#                 ans.append([merged_start, merged_end])
61#                 inserted = True
62#                 ans.extend(intervals[j:])
63#             break
64
65#         if not inserted:
66#             ans.append(newInterval)
67        
68#         return ans