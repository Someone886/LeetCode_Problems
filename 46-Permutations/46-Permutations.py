class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        ans = []
        
        if n == 0:
            return ans
        
        def helper(left, per):
            
            if len(left) == 0:
                ans.append(per.copy())
                return
            
            for index in range(len(left)):
                num = left[index]
                per.append(num)
                left_left = left[0:index] + left[index+1:]
                helper(left_left, per)
                per.pop(-1)
            
            return
        
        helper(nums, [])
        return ans