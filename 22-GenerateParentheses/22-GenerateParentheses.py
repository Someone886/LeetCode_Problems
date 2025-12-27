# Last updated: 12/27/2025, 2:43:16 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        ans = []
4        curr = []
5
6        def helper(l_left, r_left):
7            if len(curr) == n * 2:
8                ans.append("".join(curr))
9                return
10            
11            if l_left == r_left:
12                curr.append('(')
13                helper(l_left - 1, r_left)
14                curr.pop()
15
16            elif 0 < l_left < r_left:
17                curr.append('(')
18                helper(l_left - 1, r_left)
19                curr.pop()
20
21                curr.append(')')
22                helper(l_left, r_left - 1)
23                curr.pop()
24            
25            else:
26                curr.append(')')
27                helper(l_left, r_left - 1)
28                curr.pop()
29                
30        helper(n, n)
31        return ans