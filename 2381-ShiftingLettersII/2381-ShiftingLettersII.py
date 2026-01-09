# Last updated: 1/9/2026, 2:53:56 PM
1class Solution:
2    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
3        n = len(s)
4        prefix_records = [0] * n
5
6        for start, end, dr in shifts:
7            prefix = 1 if dr == 1 else -1
8            prefix_records[start] += prefix
9            if end < n - 1:
10                prefix_records[end + 1] -= prefix
11        
12        prefix_sum = 0
13        ans = list(s)
14
15        for i in range(n):
16            prefix_sum += prefix_records[i]
17
18            original_pos = ord(s[i]) - ord('a')
19            new_pos = (original_pos + prefix_sum) % 26
20            ans[i] = chr(new_pos + ord('a'))
21        
22        return "".join(ans)
23        
24
25# class Solution:
26#     def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
27#         # Convert string to a list so we can modify characters in place
28#         ans = list(s)
29
30#         for start, end, dr in shifts:
31#             # For every shift instruction, we iterate through the specified range
32#             for i in range(start, end + 1):
33#                 if dr == 1:
34#                     # Move forward: 'a' -> 'b', ..., 'z' -> 'a'
35#                     if ans[i] == 'z':
36#                         ans[i] = 'a'
37#                     else:
38#                         ans[i] = chr(ord(ans[i]) + 1)
39#                 else:
40#                     # Move backward: 'a' -> 'z', ..., 'b' -> 'a'
41#                     if ans[i] == 'a':
42#                         ans[i] = 'z'
43#                     else:
44#                         ans[i] = chr(ord(ans[i]) - 1)
45
46#         return "".join(ans)