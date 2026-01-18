# Last updated: 1/18/2026, 5:44:46 PM
1class Solution:
2    def countVowelPermutation(self, n: int) -> int:
3        dp = {}
4        MOD = 10**9 + 7
5
6        def dfs(curr_char, n_left):
7            if n_left == 0:
8                return 1
9            
10            if (curr_char, n_left) in dp:
11                return dp[(curr_char, n_left)]
12            
13            total_cnts = 0
14            match curr_char:
15                case 'a':
16                    total_cnts += dfs('e', n_left - 1)
17                case 'e':
18                    total_cnts += dfs('a', n_left - 1) + dfs('i', n_left - 1)
19                case 'i':
20                    total_cnts += dfs('a', n_left - 1) + dfs('e', n_left - 1) + \
21                                    dfs('o', n_left - 1) + dfs('u', n_left - 1)
22                case 'o':
23                    total_cnts += dfs('i', n_left - 1) + dfs('u', n_left - 1)
24                case 'u':
25                    total_cnts += dfs('a', n_left - 1)
26            
27            dp[(curr_char, n_left)] = total_cnts % MOD
28            return total_cnts
29        
30        ans = dfs('a', n - 1) + dfs('e', n - 1) + dfs('i', n - 1) + \
31                dfs('o', n - 1) + dfs('u', n - 1)
32        
33        return ans % MOD
34