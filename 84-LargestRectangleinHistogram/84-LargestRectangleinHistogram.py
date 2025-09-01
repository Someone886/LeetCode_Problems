# Last updated: 9/1/2025, 3:48:49 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            if not stack:
                # push indices not heights
                stack.append(i)
            else:
                while height < heights[stack[-1]]:
                    top_height = heights[stack.pop()]
                    # after popping, the new top is the index of the previous smaller bar
                    width = i - stack[-1] - 1   # safe because of leading 0
                    max_area = max(max_area, top_height * width)
                stack.append(i)
        
        return max_area
        