# Last updated: 11/12/2025, 2:35:06 AM
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # suppose 7 to 10 
        # 0111
        # 1000
        # 1001
        # 0010
        # key is for each bit, how large the range of (right - left) it needs to have a 0 at that bit.
        # For example, second last bit = 1 in 7, we check the last two bits = 11, 
        # then only 1 is required to add to 11 to make 100, which has 0 at that bit.
        
        res = 0

        for i in range(32):
            ith_bit = (left >> i) & 1
            if ith_bit != 1:
                continue

            # remainder = last i + 1 bits of left; All higher bits are discarded (set to 0).
            remainder = left % (1 << (i + 1))
            diff = (1 << (i + 1)) - remainder
            if right - left < diff:
                res = res | (1 << i)
        
        return res   


# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         res = 0
#         i = 0

#         while left != right:
#             left = left >> 1
#             right = right >> 1
#             i += 1
        
#         return left << i 