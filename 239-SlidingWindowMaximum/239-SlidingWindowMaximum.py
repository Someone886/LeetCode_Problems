# Last updated: 4/1/2025, 10:31:19 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque () # holds indices
        ans = []

        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()
            
            if r >= k - 1:
                ans.append(nums[q[0]])
                l += 1
        
        return ans
        