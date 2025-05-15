# Last updated: 5/14/2025, 9:30:52 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            if r == len(nums):
                break
            l += 1
            nums[l] = nums[r]
        
        return l + 1