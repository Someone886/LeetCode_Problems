# Last updated: 1/10/2026, 8:18:41 PM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        # Edge case: If we remove all digits or more, return "0"
4        if len(num) <= k:
5            return "0"
6        
7        stack = []
8        # We'll use k directly as a countdown instead of a 'removed' counter
9        
10        for char in num:
11            # While we still need to remove digits AND the current digit
12            # is smaller than the last one we added, pop the stack.
13            while stack and k > 0 and char < stack[-1]:
14                stack.pop()
15                k -= 1
16            
17            stack.append(char)
18        
19        # FIX 1: If we haven't removed k digits yet (e.g., num was "123"),
20        # remove the remaining digits from the end (the largest ones).
21        if k > 0:
22            stack = stack[:-k]
23        
24        # FIX 2: Join and remove leading zeros.
25        # Python's lstrip('0') is perfect for this.
26        ans = "".join(stack).lstrip('0')
27        
28        # If the string is empty after stripping (e.g., "000"), return "0"
29        return ans if ans else "0"