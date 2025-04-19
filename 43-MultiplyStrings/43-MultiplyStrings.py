# Last updated: 4/19/2025, 6:20:36 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return "0"
        
        ans = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        # number at i_1 * number at i_2 would produce (i_1 + i_2) of ending 0s
        for i_1 in range(len(num1)):
            for i_2 in range(len(num2)):
                digit = int(num1[i_1]) * int(num2[i_2])
                # sum the two products first, and then compute the carry-on
                ans[i_1 + i_2] += digit
                ans[i_1 + i_2 + 1] += ans[i_1 + i_2] // 10
                ans[i_1 + i_2] = ans[i_1 + i_2] % 10
        
        while ans[-1] == 0:
            ans.pop()
        ans = ans[::-1]
        
        ans = map(str, ans)
        return ''.join(ans)