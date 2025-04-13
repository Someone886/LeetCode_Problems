# Last updated: 4/12/2025, 9:22:58 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def helper(curr):
            if curr >= n:
                return 0
            
            if dp[curr] != -1:
                return dp[curr]
            
            dp[curr] = max(nums[curr] + helper(curr + 2), helper(curr + 1))
            return dp[curr]
        
        return helper(0)