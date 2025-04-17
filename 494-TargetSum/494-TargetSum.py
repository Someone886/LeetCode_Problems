# Last updated: 4/16/2025, 8:07:44 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def dfs(index, summation):
            if index >= n:
                if summation == target:
                    return 1
                else:
                    return 0
            
            if (index, summation) in dp:
                return dp[(index, summation)]
            
            dp[(index, summation)] = dfs(index + 1, summation + nums[index]) + \
                                     dfs(index + 1, summation - nums[index])
            
            return dp[(index, summation)]
        
        ans = dfs(0, 0)
        print(dp)

        return ans