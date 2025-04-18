# Last updated: 4/18/2025, 4:26:24 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10001
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum