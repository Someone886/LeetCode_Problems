# Last updated: 5/14/2025, 8:03:39 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = min(k + 1, len(nums))
        seen = set()

        for i in range(k):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        for j in range(k, len(nums)):
            seen.remove(nums[j - k])
            if nums[j] in seen:
                return True
            seen.add(nums[j])
        
        return False