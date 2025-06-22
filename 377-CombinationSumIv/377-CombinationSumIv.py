# Last updated: 6/22/2025, 2:51:24 PM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def dfs(left):
            if left == 0:
                return 1
            
            if left < 0:
                return 0
            
            if dp[left] != -1:
                return dp[left]
            
            ways = 0
            for num in nums:
                ways += dfs(left - num)
            
            dp[left] = ways
            return dp[left]
        
        ans = dfs(target)
        return ans