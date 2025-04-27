# Last updated: 4/27/2025, 2:29:07 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                        
        n = len(nums)
        k = k % n
        
        # after rotation, end of the array would be at the start.
        # therefore, first make the relative order right for the two arrays.
        reverse(nums, 0, n - 1)

        # within the first part, correct the order inside the array
        reverse(nums, 0, k - 1)

        # within the second part, correct the order inside the array
        reverse(nums, k, n - 1)
        