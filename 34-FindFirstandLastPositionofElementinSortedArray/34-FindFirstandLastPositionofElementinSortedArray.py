class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        if logn, then bts? and its sorted
        """
        if nums == []:
            return [-1, -1]
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1, -1]
        left = 0
        right = len(nums) - 1
        # index = -1 
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         # == target
        #         index = mid
        #         break
        # # print(index)
        # if index == -1:
        #     return [-1, -1]
        found = False
        left = 0
        right = len(nums) - 1
        minLeft = right
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right, minLeft, nums)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                minLeft = min(minLeft, mid)
                right = mid - 1
                found = True
            else:
                print("error")
        if not found:
            return [-1, -1]
        left = minLeft
        right = len(nums) - 1
        maxRight = minLeft
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right, maxRight, nums)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                maxRight = max(maxRight, mid)
                left = mid + 1
            else:
                print("error")
        return [minLeft, maxRight] 

        