# Last updated: 4/23/2025, 1:55:54 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        xor = n
        for i in range(n):
            xor ^= i
        
        for i in range(n):
            xor ^= nums[i]
        
        return xor