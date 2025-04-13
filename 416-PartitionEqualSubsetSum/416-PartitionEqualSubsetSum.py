# Last updated: 4/13/2025, 4:23:00 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = summation / 2

        for num in nums:
            next_dp = set()
            for s in dp:
                if s + num == target:
                    return True
                next_dp.add(s)
                next_dp.add(s + num)
            dp = next_dp
        
        return False
                