# Last updated: 6/22/2025, 2:53:30 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            
            # print(nums[l], nums[middle], nums[r])

            if nums[middle] == target:
                return middle
            
            if nums[middle] < nums[r]:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
            
            else:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
        
        return -1
        