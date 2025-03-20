class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        holders = []
        
        for token in tokens:
            if token not in operators:
                holders.append(int(token))
            else:
                ele1 = holders[-2]
                ele2 = holders[-1]
                
                if token == "+":
                    result = ele1 + ele2
                elif token == "-":
                    result = ele1 - ele2
                elif token == "*":
                    result = ele1 * ele2
                else:
                    result = int(ele1 / ele2)
                
                holders = holders[:-2] + [result]
                
            # print(holders)
        
        return holders[0]
        