# Last updated: 1/1/2026, 5:27:12 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        # 1. ADD SENTINELS:
4        # Leading 0 prevents 'stack[-1]' index errors (ensures stack is never empty).
5        # Trailing 0 forces the stack to flush/calculate all bars at the end.
6        heights = [0] + heights + [0]
7        max_area = 0
8        stack = [] # Stores indices of bars in strictly increasing height order
9
10        for i, height in enumerate(heights):
11            # 2. MONOTONIC CONDITION:
12            # If current height is smaller than the bar at the stack top,
13            # it means the 'top' bar's right boundary has been found.
14            while stack and height < heights[stack[-1]]:
15                # 3. POP AND CALCULATE:
16                # The bar we just popped is the 'height' of our rectangle.
17                top_height = heights[stack.pop()]
18                
19                # The 'width' is the distance between the current index 'i' 
20                # (right boundary) and the index now at the top of the stack 
21                # (left boundary), minus 1.
22                width = i - stack[-1] - 1
23                
24                # 4. UPDATE GLOBAL MAX:
25                max_area = max(max_area, top_height * width)
26            
27            # 5. PUSH CURRENT INDEX:
28            # We only push indices once we've maintained the monotonic property.
29            stack.append(i)
30        
31        return max_area