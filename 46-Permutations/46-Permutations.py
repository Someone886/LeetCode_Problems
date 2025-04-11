# Last updated: 4/10/2025, 8:27:31 PM
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        comb = []
        picked = [False] * len(nums)

        def helper():
            if len(comb) == len(nums):
                ans.append(comb.copy())
            
            for i in range(len(nums)):
                if picked[i]:
                    continue
                comb.append(nums[i])
                picked[i] = True
                helper()
                comb.pop()
                picked[i] = False
        
        helper()
        return ans
        