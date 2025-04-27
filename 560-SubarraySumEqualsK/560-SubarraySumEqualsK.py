# Last updated: 4/27/2025, 12:01:30 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        dp = {0:1}
        ans = 0

        for num in nums:
            pre_sum += num
            
            if pre_sum - k in dp:
                ans += dp[pre_sum-k]
            
            dp[pre_sum] = 1 + dp.get(pre_sum, 0)
        
        return ans