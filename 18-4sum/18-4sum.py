# Last updated: 6/22/2025, 2:53:35 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def k_sum(k, start, target):
            # prunning
            if len(nums) < k or start == len(nums) or nums[start] * k > target or nums[-1] * k < target:
                return []
            
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i >= start + 1 and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            else:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append(quad + [nums[l], nums[r]])
                        while l + 1 < r and nums[l + 1] == nums[l]:
                            l += 1
                        l += 1
                        
                        while l < r - 1 and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                        
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1

                return
        
        k_sum(4, 0, target)
        return res