# Last updated: 6/22/2025, 2:53:26 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        temp = 0

        start = 0
        n = len(height)

        while start < n - 1:
            start_height = height[start]

            next_bar = start + 1
            next_height = height[next_bar]

            while next_bar < n- 1 and next_height < start_height:
                temp += start_height - next_height
                next_bar += 1
                next_height = height[next_bar]
            
            if next_height >= start_height:
                total += temp
                start = next_bar
                temp = 0

            else:
                break

        end = start
        start = n-1

        while start > end:
            start_height = height[start]

            next_bar = start - 1
            next_height = height[next_bar]

            temp = 0
            
            while next_bar >= end and next_height < start_height:
                temp += start_height - next_height
                next_bar -= 1
                next_height = height[next_bar]
            
            total += temp
            start = next_bar
            temp = 0
        
        return total