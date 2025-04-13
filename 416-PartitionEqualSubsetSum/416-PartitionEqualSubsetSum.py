# Last updated: 4/13/2025, 4:12:00 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 == 1:
            return False
        
        n = len(nums)
        target = summation // 2
        
        dp = [[-1] * target for _ in range(n)]

        def helper(index, curr_sum):
            if curr_sum == target:
                return True
            
            if index >= n or curr_sum > target:
                return False
            
            if dp[index][curr_sum] != -1:
                return dp[index][curr_sum]
            
            dp[index][curr_sum] = helper(index + 1, curr_sum + nums[index]) or helper(index + 1, curr_sum)
            
            return dp[index][curr_sum]
        
        return helper(0, 0)