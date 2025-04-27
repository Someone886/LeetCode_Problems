class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1) Place each number v in position v-1 if possible
        for i in range(n):
            # swap unless nums[i] = v is out of range or the current slot is correct
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # 2) Find first position where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # all 1…n are present
        return n + 1