# Last updated: 4/10/2025, 9:57:44 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        ans = []
        n = len(nums)
        subset = []

        nums.sort()

        def helper(index):
            if index > n - 1:
                ans.append(subset.copy())
                return
            
            subset.append(nums[index])
            helper(index + 1)
            subset.pop()

            # if we don't take the num at the first position (index),
            # then we should not take its duplicates either.
            # instead, take the one after its duplicates.

            index += 1
            while index < n and nums[index] == nums[index - 1]:
                index += 1
            
            helper(index)
        
        helper(0)
        return ans
        