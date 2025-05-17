# Last updated: 5/17/2025, 12:46:03 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 and j >= 0:
            digit_a = int(a[i])
            digit_b = int(b[j])

            current_sum = digit_a + digit_b + carry
            result.append(str(current_sum % 2))
            carry = current_sum // 2

            i -= 1
            j -= 1

        while i >= 0:
            digit_a = int(a[i])
            current_sum = digit_a + carry
            result.append(str(current_sum % 2))
            carry = current_sum // 2
            i -= 1

        while j >= 0:
            digit_b = int(b[j])
            current_sum = digit_b + carry
            result.append(str(current_sum % 2))
            carry = current_sum // 2
            j -= 1

        if carry:
            result.append('1')

        result.reverse()

        return "".join(result)