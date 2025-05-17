# Last updated: 5/17/2025, 12:04:43 AM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        seen = []

        for op in operations:
            if op == "+":
                prev1 = seen[-1]
                prev2 = seen[-2]
                seen.append(prev1 + prev2)
            elif op == "D":
                seen.append(seen[-1] * 2)
            elif op == "C":
                seen.pop()
            else:
                seen.append(int(op))
        
        return sum(seen)