# Last updated: 11/17/2025, 1:18:06 AM
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        curr = []

        def break_at(index):
            if index == len(s):
                if len(curr) == 4:
                    ans.append(".".join(curr))
                return
            
            if len(curr) == 4:
                return
            
            for i in range(1, 4):
                if index + i > len(s):
                    return
                
                next_int = s[index:index + i]
                
                if next_int == "0":
                    curr.append(next_int)
                    break_at(index + i)
                    curr.pop()
                    return
                
                if int(next_int) <= 255:
                    curr.append(next_int)
                    break_at(index + i)
                    curr.pop()
                else:
                    break
        
        break_at(0)

        return ans