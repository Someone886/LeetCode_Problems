# Last updated: 6/22/2025, 2:52:12 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_1 = [-1] * (n - 1)
        dp_2 = [-1] * (n - 2)

        def helper(curr, dp, nums):
            if curr >= len(nums):
                return 0
            
            if dp[curr] != -1:
                return dp[curr]
            
            dp[curr] = max(nums[curr] + helper(curr + 2, dp, nums), helper(curr + 1, dp, nums))
            return dp[curr]
        
        ans = max(helper(0, dp_1, nums[1:]), nums[0] + helper(0, dp_2, nums[2:-1]))

        return ans