# Last updated: 6/22/2025, 2:50:38 PM
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index, total):
            if index == len(nums):
                return total
            
            return dfs(index + 1, total ^ nums[index]) + dfs(index + 1, total)
        
        return dfs(0, 0)
