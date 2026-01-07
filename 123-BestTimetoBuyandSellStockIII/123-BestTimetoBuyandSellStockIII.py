# Last updated: 1/7/2026, 12:09:55 AM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        # dp stores results for (index_s, index_p) to avoid redundant recursive calls
4        dp = {}
5
6        def helper(index_s, index_p):
7            # BASE CASE 1: Both string and pattern are fully processed
8            if index_s == len(s) and index_p == len(p):
9                return True
10            
11            # BASE CASE 2: Pattern is exhausted, but string still has characters
12            if index_p >= len(p):
13                return False
14            
15            # MEMOIZATION: Return already computed result for this state
16            if (index_s, index_p) in dp:
17                return dp[(index_s, index_p)]
18            
19            # SPECIAL CASE: String is empty, but pattern is not
20            if index_s == len(s):
21                # We can only match an empty string if the remaining pattern 
22                # follows the "char*" format (allowing us to treat it as zero chars).
23                if index_p < len(p) - 1 and p[index_p + 1] == "*":
24                    dp[(index_s, index_p)] = helper(index_s, index_p + 2)
25                    return dp[(index_s, index_p)]
26                else:
27                    return False
28            
29            # RECURSIVE LOGIC FOR '*' (Quantifier)
30            # Peek ahead to see if the next character in the pattern is '*'
31            if index_p < len(p) - 1 and p[index_p + 1] == "*":
32                # Check if current character matches (literally or via '.')
33                match = (p[index_p] == '.' or s[index_s] == p[index_p])
34                
35                if match:
36                    # Choice 1: Use '*' to consume current char (helper(index_s + 1, index_p))
37                    # Choice 2: Ignore '*' and the char before it (helper(index_s, index_p + 2))
38                    dp[(index_s, index_p)] = helper(index_s + 1, index_p) or \
39                                             helper(index_s, index_p + 2)
40                else:
41                    # If no match, we MUST treat 'char*' as zero characters
42                    dp[(index_s, index_p)] = helper(index_s, index_p + 2)
43            
44            # RECURSIVE LOGIC FOR '.' or Literal Match
45            else:
46                if (p[index_p] == '.' or s[index_s] == p[index_p]):
47                    # Match found, move both pointers forward
48                    dp[(index_s, index_p)] = helper(index_s + 1, index_p + 1)
49                else:
50                    # Mismatch found with no wildcard '*' to save us
51                    dp[(index_s, index_p)] = False
52            
53            return dp[(index_s, index_p)]
54        
55        return helper(0, 0)