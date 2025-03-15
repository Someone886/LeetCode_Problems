class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while (left <= right):
            middle = left + (right - left) // 2
            if middle * middle > x:
                right = middle - 1
            else:
                left = middle + 1
        
        return right