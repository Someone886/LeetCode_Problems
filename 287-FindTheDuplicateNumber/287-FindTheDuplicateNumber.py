# Last updated: 6/22/2025, 2:58:52 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            key = nums[i]

            if key < 0:
                key = -key
            
            key = key - 1
            
            val = nums[key]
            if val < 0:
                return key + 1
            else:
                nums[key] *= -1
        