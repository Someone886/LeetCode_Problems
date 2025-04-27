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