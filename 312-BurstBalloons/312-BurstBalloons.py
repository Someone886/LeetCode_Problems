# Last updated: 4/17/2025, 3:07:22 AM
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # DP = [left boundary][right boundary] of a subarray
        # Pointer i = index of the last popped balloon in a subarray
        # l, r inclusively

        dp = {}
        nums = [1] + nums + [1]

        def helper(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                value = nums[i] * nums[l - 1] * nums[r + 1]
                value += helper(l, i - 1) + helper(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], value)
            
            return dp[(l, r)]
        
        return helper(1, len(nums) - 2)