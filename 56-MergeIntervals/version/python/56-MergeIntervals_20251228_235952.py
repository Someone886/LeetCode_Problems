# Last updated: 12/28/2025, 11:59:52 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key = lambda x: x[0])
4        ans = []
5
6        for interval in intervals:
7            if not ans or ans[-1][1] < interval[0]:
8                ans.append(interval)
9            else:
10                ans[-1][1] = max(ans[-1][1], interval[1])
11        
12        return ans
13