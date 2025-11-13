# Last updated: 11/13/2025, 2:14:33 AM
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        max_len = r - l
        sign = ""

        while r < len(arr):
            curr_value = arr[r]
            prev_value = arr[r - 1]

            # fresh start
            if sign == "":
                if curr_value > prev_value:
                    r += 1
                    sign = "<"
                    max_len = max(max_len, r - l)
                elif curr_value < prev_value:
                    r += 1
                    sign = ">"
                    max_len = max(max_len, r - l)
                    
                # if curr == prev at the fresh start, then slide the window to the right by 1
                else:
                    l = r
                    r += 1
            elif sign == "<":
                if curr_value < prev_value:
                    r += 1
                    sign = ">"
                    max_len = max(max_len, r - l)
                
                # if inequality does not hold, then set l = r - 1 as the new start
                else:
                    l = r - 1
                    sign = ""
            else:
                if curr_value > prev_value:
                    r += 1
                    sign = "<"
                    max_len = max(max_len, r - l)
                else:
                    l = r - 1
                    sign = ""
        
        return max_len   