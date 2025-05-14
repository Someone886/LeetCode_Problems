# Last updated: 5/14/2025, 6:52:26 PM
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index, total):
            if index == len(nums):
                return total
            
            return dfs(index + 1, total ^ nums[index]) + dfs(index + 1, total)
        
        return dfs(0, 0)
