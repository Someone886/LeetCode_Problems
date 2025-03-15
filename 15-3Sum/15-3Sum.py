class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        n = len(nums)
        
        for index, num in enumerate(nums):
            if num > 0:
                break
                
            if index > 0 and nums[index - 1] == num:
                continue
            
            left = index + 1
            right = n - 1
            
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
                    
                elif three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
    
        return ans
        