# Last updated: 6/22/2025, 2:53:29 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        l, r = 0, len(nums) - 1

        last_l = -1
        last_r = -1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                last_l = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                last_r = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return [last_l, last_r]