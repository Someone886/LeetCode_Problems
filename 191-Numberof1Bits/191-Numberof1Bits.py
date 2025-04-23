# Last updated: 4/22/2025, 11:02:24 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        cnt = 0

        for i in range(32):
            cnt += mask & (n >> i) 
        
        return cnt