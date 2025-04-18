# Last updated: 4/17/2025, 10:29:34 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        cnt = 0
        prev_end = -50001

        for interval in intervals:
            if interval[0] < prev_end:
                prev_end = min(prev_end, interval[1])
                cnt += 1
            else:
                prev_end = interval[1]
        
        return cnt