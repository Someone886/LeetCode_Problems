# Last updated: 4/10/2025, 6:59:56 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        ans = []
        n = len(nums)
        subset = []

        def helper(index):
            if index >= n:
                ans.append(subset.copy())
                return

            subset.append(nums[index])
            helper(index + 1)
            subset.pop()
            helper(index + 1)
        
        helper(0)
        return ans