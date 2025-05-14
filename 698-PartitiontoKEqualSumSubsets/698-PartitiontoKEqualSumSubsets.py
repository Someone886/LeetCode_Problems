# Last updated: 5/13/2025, 11:33:37 PM
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        
        if nums_sum % k:
            return False
        
        subset_target = nums_sum // k
        subset_sums = [0] * k

        nums.sort(reverse=True)

        def backtrack(index):
            if index == len(nums):
                return True
            
            for j in range(k):
                if subset_sums[j] + nums[index] <= subset_target:
                    subset_sums[j] += nums[index]
                    if backtrack(index + 1):
                        return True
                    subset_sums[j] -= nums[index]

                    if subset_sums[j] == 0:
                        return False
            
            return False
        
        return backtrack(0)
