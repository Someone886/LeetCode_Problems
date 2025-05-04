# Last updated: 5/4/2025, 12:48:20 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            print(nums[l], nums[m], nums[r])

            if nums[m] == target:
                return True
            
            # if we can't tell which side is sorted, shrink both ends
            if nums[l] == nums[m]:
                l += 1
            elif nums[r] == nums[m]:
                r -= 1
            
            # Right half [m..r] is sorted
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            # left half [l..m] is sorted
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return False