# Last updated: 5/18/2025, 2:16:16 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l