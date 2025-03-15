class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        if n == 0:
            ans.append([])
            return ans
        
        def helper(left, length, subset):
            
            if length == 0:
                ans.append(subset.copy())
                return
            
            for index in range(len(left)):
                element = left[index]
                left_left = left[index+1:]
                subset.append(element)
                helper(left_left, length - 1, subset)
                subset.pop(-1)
            
            return
        
        for i in range(0, len(nums) + 1):
            helper(nums, i, [])
            
        return ans