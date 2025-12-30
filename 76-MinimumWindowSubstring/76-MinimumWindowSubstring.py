# Last updated: 12/30/2025, 1:32:07 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        # Base case: if s is shorter than t, it's impossible to find t in s
4        if len(s) < len(t):
5            return ''
6        
7        # Dictionary to store the frequency of characters required from t
8        dic = {}
9        for char in t:
10            dic[char] = 1 + dic.get(char, 0)
11        
12        # need_cnt: total unique characters in t that must be satisfied
13        # satisfied_cnt: how many unique characters currently meet the required frequency
14        need_cnt = len(dic)
15        satisfied_cnt = 0
16        seen_cnt = {}
17
18        start = 0
19        end = 0
20        n = len(s)
21
22        # Initialize min_size with a value larger than any possible answer
23        min_size = len(s) + 1
24        min_range = [-1, -1]
25
26        # Expand the window by moving the 'end' pointer
27        while end < n:
28            char = s[end]
29            if char in dic:
30                seen_cnt[char] = 1 + seen_cnt.get(char, 0)
31
32                # If the current character count matches the required count in t
33                if seen_cnt[char] == dic[char]:
34                    satisfied_cnt += 1
35
36            # While the current window contains all characters of t
37            while satisfied_cnt == need_cnt:
38                # Update the result if this window is smaller than the previous minimum
39                current_window_size = end - start + 1
40                if current_window_size < min_size:
41                    min_size = current_window_size
42                    min_range = [start, end + 1] # Store range for slicing
43                
44                # Try to shrink the window from the left to find a smaller valid window
45                left_char = s[start]
46                if left_char in dic:
47                    seen_cnt[left_char] -= 1
48                    # If removing this char breaks the "satisfied" condition
49                    if seen_cnt[left_char] < dic[left_char]:
50                        satisfied_cnt -= 1
51                
52                start += 1 # Move the left boundary forward
53            
54            end += 1 # Move the right boundary forward
55        
56        # If min_range was never updated, return empty string; else return the slice
57        return s[min_range[0]:min_range[1]] if min_range[0] != -1 else ""
58