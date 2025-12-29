# Last updated: 12/28/2025, 11:08:44 PM
1# class Solution:
2#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3#         ans = []
4#         i = 0
5#         n = len(intervals)
6#         new_start, new_end = newInterval
7
8#         # 1. Add all intervals that come strictly BEFORE the new interval
9#         while i < n and intervals[i][1] < new_start:
10#             ans.append(intervals[i])
11#             i += 1
12
13#         # 2. Merge all overlapping intervals
14#         # An overlap exists if the current interval starts before or at new_end
15#         while i < n and intervals[i][0] <= new_end:
16#             new_start = min(new_start, intervals[i][0])
17#             new_end = max(new_end, intervals[i][1])
18#             i += 1
19        
20#         # Add the final merged interval
21#         ans.append([new_start, new_end])
22
23#         # 3. Add all remaining intervals that come strictly AFTER
24#         ans.extend(intervals[i:])
25
26#         return ans
27
28
29class Solution:
30    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
31        ans = []
32        new_start, new_end = newInterval
33        inserted = False
34        i = 0
35        n = len(intervals)
36
37        while i < n:
38            start_i, end_i = intervals[i]
39
40            if end_i < new_start:
41                ans.append(intervals[i])
42                i += 1
43            else:
44                break
45        
46        # If an interval is found with end_i includes new_start
47        if i < n:
48            merged_start = min(intervals[i][0], new_start)
49
50            # Find the first interval with end_i includes new_end
51            while i < len(intervals) and intervals[i][1] <= new_end:
52                i += 1
53
54            # If no such interval exists
55            if i == len(intervals):
56                merged_end = new_end
57                ans.append([merged_start, merged_end])
58                inserted = True
59            # If new_end is within start_i and end_i
60            elif new_end >= intervals[i][0]:
61                merged_end = intervals[i][1]
62                ans.append([merged_start, merged_end])
63                inserted = True
64                ans.extend(intervals[i + 1:])
65            # if new_end is before start_i
66            else:
67                merged_end = new_end
68                ans.append([merged_start, merged_end])
69                inserted = True
70                ans.extend(intervals[i:])
71
72        # If no interval found to include new_start, then append new interval to the end
73        if not inserted:
74            ans.append(newInterval)
75        
76        return ans