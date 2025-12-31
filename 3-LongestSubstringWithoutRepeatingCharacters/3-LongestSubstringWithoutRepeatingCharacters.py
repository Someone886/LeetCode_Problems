# Last updated: 12/30/2025, 9:28:00 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        if not s or len(s) == 0:
4            return 0
5        
6        start = 0
7        end = 1
8        max_length = 1
9
10        seen = set(s[0])
11
12        while end < len(s):
13            if s[end] in seen:
14                max_length = max(max_length, end - start)
15
16                while s[start] != s[end]:
17                    seen.remove(s[start])
18                    start += 1
19                seen.remove(s[start])
20                start += 1
21
22            seen.add(s[end])
23            end += 1
24        
25        return max(max_length, len(seen))
26
27'''
28class Solution(object):
29    def lengthOfLongestSubstring(self, s):
30        """
31        :type s: str
32        :rtype: int
33        """
34        if len(s) == 0:
35            return 0
36        
37        max_length = 0
38        length = 0
39        left, right = 0, 1
40        n = len(s)
41        hash_map = {}
42        
43        while left < n and right <= n:
44            c = s[right - 1]
45            if c in hash_map and hash_map[c] >= left:
46                left = hash_map[c] + 1
47
48            hash_map[c] = right - 1
49            if right - left > max_length:
50                max_length = right - left
51
52            right += 1
53
54        return max_length
55'''