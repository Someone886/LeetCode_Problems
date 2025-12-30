# Last updated: 12/30/2025, 1:54:25 AM
1from collections import Counter
2
3class Solution:
4    def findAnagrams(self, s: str, p: str) -> List[int]:
5        # Count frequencies of characters needed for an anagram
6        count = Counter(p)
7
8        # need_cnt: number of unique characters in p that must meet a specific frequency
9        need_cnt = len(count)
10        satisfied_cnt = 0
11        seen_dic = {}
12
13        ans = []
14
15        # Define the fixed window size (length of p)
16        start = 0
17        end = start + len(p)
18
19        # 1. Initial State: Process the very first window of length p
20        seen_dic = Counter(s[start:end])
21        for char in seen_dic.keys():
22            if char in count:
23                # If current window count matches required count for a char
24                if count[char] == seen_dic[char]:
25                    satisfied_cnt += 1
26        
27        # Check if the first window is an anagram
28        if satisfied_cnt == need_cnt:
29            ans.append(start)
30
31        # 2. Sliding Window: Move the window one character at a time
32        while end < len(s):
33            # --- Removing the character that is sliding OUT (s[start]) ---
34            # If the character leaving was part of our requirement
35            if s[start] in count:
36                # If it WAS satisfied, it's about to be broken
37                if seen_dic[s[start]] == count[s[start]]:
38                    satisfied_cnt -= 1
39                # If removing it makes it match the count (e.g., it was over-represented)
40                elif seen_dic[s[start]] == count[s[start]] + 1:
41                    satisfied_cnt += 1
42            
43            seen_dic[s[start]] -= 1
44            start += 1 # Shrink left
45            
46            # --- Adding the character that is sliding IN (s[end]) ---
47            char_in = s[end]
48            seen_dic[char_in] = seen_dic.get(char_in, 0) + 1
49            
50            if char_in in count:
51                # If adding it makes the count perfect
52                if seen_dic[char_in] == count[char_in]:
53                    satisfied_cnt += 1
54                # If adding it makes the count exceed what we need
55                elif seen_dic[char_in] == count[char_in] + 1:
56                    satisfied_cnt -= 1
57            
58            end += 1 # Expand right
59
60            # 3. Validation: If satisfied_cnt matches need_cnt, we found an anagram
61            if satisfied_cnt == need_cnt:
62                ans.append(start)
63        
64        return ans
65        