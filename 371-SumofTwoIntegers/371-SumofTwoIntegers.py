class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        # Why mask? In Python, integers are of arbitrary precision.
        mask = 0xffffffff

        # logic:
        # a + b without carry = a ^ b
        # carry = (a & b) << 1
        # a + b -> a ^ b + carry -> (a ^ b) ^ ((a & b) << 1) -> continue if carry remains
        
        # Iterate till there is no carry 
        while (b & mask) != 0:

            # carry contains common set bits of a and b, left shifted by 1
            carry = (a & b) << 1

            # Update a with (a + b without carry)
            a = a ^ b

            # Update b with carry
            b = carry 

        return a & mask if b > 0 else a