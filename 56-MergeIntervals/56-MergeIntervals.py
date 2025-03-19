class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        ans = []

        for interval in sorted_intervals:
            if len(ans) == 0:
                ans.append(interval)
            
            last_interval = ans[-1]
            
            if last_interval[1] >= interval[0]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                ans.append(interval)
        
        return ans