# Last updated: 4/13/2025, 8:15:41 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        pre = post = 0

        for i in range(n):
            pre = nums[i] * (pre or 1)
            post = nums[n - 1 - i] * (post or 1)
            ans = max(ans, max(pre, post))
        
        return ans