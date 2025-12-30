# Last updated: 12/30/2025, 2:53:43 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        # Pointers for the sliding window
4        start = 0
5        end = 1
6        
7        # Track the frequency of the most frequent character in the current window
8        most_frequent_cnt = 1
9        # Track the maximum valid window size found so far
10        max_length = 1
11
12        # Frequency map for characters within the current window
13        window_cnt = {s[start]:1}
14
15        while end < len(s):
16            # Expand the window: include s[end] and update its frequency
17            window_cnt[s[end]] = 1 + window_cnt.get(s[end], 0)
18            
19            # Update the count of the most frequent character in the current window
20            most_frequent_cnt = max(most_frequent_cnt, window_cnt[s[end]])
21            
22            # The number of characters to replace is (window_size - most_frequent_cnt)
23            # If replacements needed > k, the window is invalid; shrink from the left
24            if end + 1 - start - most_frequent_cnt > k:
25                # Update max_length before shrinking (using the size before adding s[end])
26                max_length = max(max_length, end - start)
27                
28                # Shrink the window: remove s[start] and move the start pointer forward
29                window_cnt[s[start]] -= 1
30                start += 1
31
32            end += 1
33
34        # Final check: the loop might end with a valid window that hasn't been recorded
35        if end - start - most_frequent_cnt <= k:
36            max_length = max(max_length, end - start)
37
38        return max_length