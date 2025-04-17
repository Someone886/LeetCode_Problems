# Last updated: 4/17/2025, 3:47:00 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        l, r = 0, n - 1
        found_index = -1

        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] == target:
                found_index = mid + 1
                break

            elif intervals[mid][0] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        if found_index == -1:
            found_index = r + 1

        intervals = intervals[:found_index] + [newInterval] + intervals[found_index:]

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res