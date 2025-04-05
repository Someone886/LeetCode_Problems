# Last updated: 4/5/2025, 3:32:02 AM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2          # A is the shorter array
        total = len(A) + len(B)
        half = total // 2

        if len(nums1) > len(nums2):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2          # middle pointer for A
            j = half - i - 2          # pointer for B

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 <= len(A) - 1 else float("inf")

            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 <= len(B) - 1 else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # odd 
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left)) / 2
            
            elif A_left > B_right:
                r = i - 1
            
            else: # B_left > A_right
                l = i + 1