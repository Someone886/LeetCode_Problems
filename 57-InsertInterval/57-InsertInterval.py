# Last updated: 4/17/2025, 3:37:15 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        target_index = -1
        if intervals[0][0] >= newInterval[0]:
            target_index = -1
        
        elif intervals[len(intervals) - 1][0] <= newInterval[0]:
            target_index = len(intervals) - 1
        
        else:
            for i in range(len(intervals) - 1):
                if intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
                    target_index = i
                    break

        intervals = intervals[:target_index + 1] + [newInterval] + intervals[target_index + 1:]
        
        if target_index == -1:
            target_index = 0

        j = target_index

        while j < len(intervals) - 1:
            curr = intervals[j]
            nxt = intervals[j + 1]

            if curr[1] >= nxt[0]:
                intervals[j] = [curr[0], max(curr[1], nxt[1])]
                intervals.pop(j + 1)
            else:
                j += 1

        return intervals