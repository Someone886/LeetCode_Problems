# Last updated: 4/29/2025, 9:12:36 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = ''

        for char in s:
            if char.isdigit():
                number += char
            elif char.isalpha():
                stack.append(char)
            elif char == "[":
                stack.append(number)
                number = ''
            else:                       # char == ']'
                tail = ''
                while stack and not stack[-1].isdigit():
                    last_char = stack.pop()
                    tail = last_char + tail
                num = int(stack.pop())
                stack.append(num * tail)
        
        return ''.join(stack)