# Last updated: 6/22/2025, 2:52:24 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        holders = []
        
        for token in tokens:
            if token not in operators:
                holders.append(int(token))
            else:
                ele2 = holders.pop()
                ele1 = holders.pop()
                
                if token == "+":
                    result = ele1 + ele2
                elif token == "-":
                    result = ele1 - ele2
                elif token == "*":
                    result = ele1 * ele2
                else:
                    result = int(ele1 / ele2)
                
                holders.append(result)

            # print(holders)
        
        return holders[0]
        