# Last updated: 4/13/2025, 8:29:08 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        most_positive = 1
        most_negative = 1

        for num in nums:
            temp = num * most_positive
            
            # if num is the largest, we can just ignore everything before it
            most_positive = max(temp, num * most_negative, num)
            most_negative = min(temp, num * most_negative, num)

            # keep the largest number in the ans
            ans = max(ans, most_positive)
        
        return ans
        