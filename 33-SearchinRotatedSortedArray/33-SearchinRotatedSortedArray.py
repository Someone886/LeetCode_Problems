class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                if target == nums[l]:
                    return l

                if target < nums[l] and nums[mid] >= nums[l]:
                    l = mid + 1
                elif target < nums[l] and nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    r = mid - 1
            
            elif nums[mid] < target:
                if target == nums[l]:
                    return l

                if target > nums[l] and nums[mid] >= nums[l]:
                    l = mid + 1
                elif target > nums[l] and nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1