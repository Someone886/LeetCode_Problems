# Last updated: 1/6/2026, 3:32:15 PM
1class Solution:
2    def longestStrChain(self, words: List[str]) -> int:
3        words.sort(key = lambda x: len(x))
4        dp = {}
5
6        for word in words:
7            dp[word] = 1
8
9            for i in range(len(word)):
10                potential_predecessor = word[:i] + word[i+1:]
11                if potential_predecessor in dp:
12                    dp[word] = max(dp[word], dp[potential_predecessor] + 1)
13        
14        return max(dp.values())