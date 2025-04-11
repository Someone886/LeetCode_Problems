# Last updated: 4/10/2025, 9:42:07 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        ans = []
        n = len(nums)
        subset = []

        nums.sort()

        def helper(index):
            ans.append(subset.copy())
            
            for i in range(index + 1, len(nums)):

                # if we don't take the num at the first position (index + 1),
                # then we should not take its duplicates either.
                if i > index + 1 and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                helper(i)
                subset.pop()
        
        helper(-1)
        return ans
        