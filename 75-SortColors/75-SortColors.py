class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map = {0:0, 1:0, 2:0}
        
        for ele in nums:
            hash_map[ele] += 1
        
        for i in range(len(nums)):
            if i < hash_map[0]:
                nums[i] = 0
            elif i < hash_map[0] + hash_map[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        