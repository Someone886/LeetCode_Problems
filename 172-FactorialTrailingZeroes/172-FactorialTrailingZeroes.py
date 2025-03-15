class Solution:
    def trailingZeroes(self, n: int) -> int:
        nums = 0
        
        while n != 0:
            nums += n // 5
            n = n // 5
        
        return nums