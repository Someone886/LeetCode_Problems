# Last updated: 4/23/2025, 3:06:09 AM
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        ans = 0

        while x != 0:
            if ans > MAX // 10 or ans < MIN // 10:
                return 0
            
            # to handle negative x cuz of Python's weird behaviors
            last_digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if ans == MAX // 10 and last_digit > MAX % 10:
                return 0
            
            if ans == MIN // 10 and last_digit < MIN & 10:
                return 0

            ans = ans * 10 + last_digit

        return ans