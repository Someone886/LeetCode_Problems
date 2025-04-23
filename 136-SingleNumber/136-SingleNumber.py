# Last updated: 4/22/2025, 10:58:40 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res