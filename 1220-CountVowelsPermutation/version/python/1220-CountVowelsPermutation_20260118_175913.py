# Last updated: 1/18/2026, 5:59:13 PM
1class Solution:
2    def countVowelPermutation(self, n: int) -> int:
3        MOD = 10**9 + 7
4        
5        # Initial counts for n = 1
6        a, e, i, o, u = 1, 1, 1, 1, 1
7        
8        for _ in range(1, n):
9            # Calculate next counts based on which vowels can lead to the current one
10            # Rules reversed (Who can lead to 'a'? 'e', 'i', 'u' etc.)
11            next_a = (e + i + u) % MOD
12            next_e = (a + i) % MOD
13            next_i = (e + o) % MOD
14            next_o = i
15            next_u = (i + o) % MOD
16            
17            # Update variables for the next iteration
18            a, e, i, o, u = next_a, next_e, next_i, next_o, next_u
19            
20        return (a + e + i + o + u) % MOD
21
22
23# class Solution:
24#     def countVowelPermutation(self, n: int) -> int:
25#         dp = {}
26#         MOD = 10**9 + 7
27
28#         def dfs(curr_char, n_left):
29#             if n_left == 0:
30#                 return 1
31            
32#             if (curr_char, n_left) in dp:
33#                 return dp[(curr_char, n_left)]
34            
35#             total_cnts = 0
36#             match curr_char:
37#                 case 'a':
38#                     total_cnts += dfs('e', n_left - 1)
39#                 case 'e':
40#                     total_cnts += dfs('a', n_left - 1) + dfs('i', n_left - 1)
41#                 case 'i':
42#                     total_cnts += dfs('a', n_left - 1) + dfs('e', n_left - 1) + \
43#                                     dfs('o', n_left - 1) + dfs('u', n_left - 1)
44#                 case 'o':
45#                     total_cnts += dfs('i', n_left - 1) + dfs('u', n_left - 1)
46#                 case 'u':
47#                     total_cnts += dfs('a', n_left - 1)
48            
49#             dp[(curr_char, n_left)] = total_cnts % MOD
50#             return total_cnts
51        
52#         ans = dfs('a', n - 1) + dfs('e', n - 1) + dfs('i', n - 1) + \
53#                 dfs('o', n - 1) + dfs('u', n - 1)
54        
55#         return ans % MOD
56