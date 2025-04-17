# Last updated: 4/16/2025, 8:10:57 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def dfs(index, summation):
            if index == n:
                return 1 if summation == target else 0
            
            if (index, summation) in dp:
                return dp[(index, summation)]
            
            dp[(index, summation)] = dfs(index + 1, summation + nums[index]) + \
                                     dfs(index + 1, summation - nums[index])
            
            return dp[(index, summation)]
        
        ans = dfs(0, 0)

        return ans
