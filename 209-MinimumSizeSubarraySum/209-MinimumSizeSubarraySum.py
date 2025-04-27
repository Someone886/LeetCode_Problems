# Last updated: 4/27/2025, 4:09:03 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_length = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if min_length == float("inf") else min_length

'''
non-optimal version but same complexity

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1
        summation = nums[0]
        length = 1
        min_length = float("inf")
        n = len(nums)

        if summation >= target:
            return 1

        while r < n:
            while summation < target and r < n:
                summation += nums[r]
                r += 1
                length += 1 
            
            while summation >= target:
                min_length = min(length, min_length)
                summation -= nums[l]
                l += 1
                length -= 1
            
            if l == r:
                break
        
        return min_length if min_length != float("inf") else 0
'''
