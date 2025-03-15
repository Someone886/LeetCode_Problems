class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        remainders = {}

        idx = 2
        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = idx
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))
            idx += 1
        
        if remainder in remainders:
            result.insert(remainders[remainder], '(')
            result.append(')')
        
        # print(result)

        return ''.join(result).rstrip(".")