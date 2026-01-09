# Last updated: 1/9/2026, 1:56:22 AM
1class Solution:
2    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
3        res = []
4
5        for word in words:
6            # pattern_mapping tracks: pattern_char -> word_char
7            pattern_mapping = {}
8            # seen tracks: word_chars already mapped to something in the pattern
9            seen = set()
10            match = True
11
12            for i in range(len(pattern)):
13                w = word[i]
14                c = pattern[i]
15
16                # CASE 1: The word character has been used before
17                if w in seen:
18                    # If it was used, it MUST be mapped to the current pattern char 'c'
19                    if c in pattern_mapping and pattern_mapping[c] == w:
20                        continue
21                    else:
22                        # Conflict: word char 'w' is already mapped to a different pattern char
23                        match = False
24                        break
25                
26                # CASE 2: Pattern char 'c' is already mapped to a different word char
27                elif c in pattern_mapping and pattern_mapping[c] != w:
28                    match = False
29                    break
30                
31                # CASE 3: Redundant check (pattern_mapping[c] == w is already covered)
32                elif c in pattern_mapping and pattern_mapping[c] == w:
33                    continue
34                
35                # CASE 4: New mapping discovery
36                else:
37                    # 'c' is new and 'w' hasn't been seen; create the link
38                    pattern_mapping[c] = w
39                    seen.add(w)
40            
41            if match:
42                res.append(word)
43        
44        return res