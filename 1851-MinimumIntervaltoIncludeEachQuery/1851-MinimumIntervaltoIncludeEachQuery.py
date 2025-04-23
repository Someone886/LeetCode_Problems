class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r)) 
                i += 1
            
            # even if there are queries left in min_heap that does not contain q,
            # we don't care as the only thing that matters to q is min_heap[0]
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            res[q] = min_heap[0][0] if min_heap else -1
        
        ans = []
        for q in queries:
            ans.append(res[q])
        
        return ans