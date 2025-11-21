# Last updated: 11/20/2025, 8:16:52 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            l_height = height[l]
            r_height = height[r]

            area = (r - l) * min(l_height, r_height)
            if area > max_area:
                max_area = area

            if l_height <= r_height:
                l += 1
            else:
                r -= 1
        
        return max_area