# Last updated: 4/1/2025, 10:19:37 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i in range(0, k):
            heapq.heappush(heap, (-nums[i], i))
        
        ans.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            ans.append(-heap[0][0])
        
        return ans
        