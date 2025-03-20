class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()

        for i in tokens:
            if i in '+-*/':
                num2 = st.pop()
                num1 = st.pop()
                if i == '+':
                    num3 = num1 + num2
                elif i == '-':
                    num3 = num1 - num2
                elif i == '*':
                    num3 = num1 * num2
                else:
                    num3 = int(num1 / num2)
                st.append(num3)
                #print(num1, i, num2, '=', num3)
            else:
                num3 = int(i)
                st.append(num3)
        return st[-1]