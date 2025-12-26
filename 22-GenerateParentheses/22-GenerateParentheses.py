# Last updated: 12/26/2025, 6:23:17 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        if not s or len(s) == 0:
4            return True
5        n = len(s)
6        dp = {}
7
8        def fit_words(index):
9            if index == n:
10                return True
11            
12            if index in dp:
13                return dp[index]
14            
15            can_fit = False
16            for word in wordDict:
17                m = len(word)
18                if s[index:index+m] == word:
19                    can_fit = fit_words(index + m)
20                    if can_fit:
21                        break
22            
23            dp[index] = can_fit
24            
25            return dp[index]
26        
27        return fit_words(0)