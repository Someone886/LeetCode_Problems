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
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                l = mid - 1
                r = mid + 1
                while l >= 0 and nums[l] == target:
                    l -= 1
                l += 1
                
                while r < len(nums) and nums[r] == target:
                    r += 1
                r -= 1
                
                return [l, r]
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return [-1, -1]