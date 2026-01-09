# Last updated: 1/9/2026, 1:28:16 AM
1class Solution:
2    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
3        # 1. Create a lookup table for valid operations
4        # We store -1 to mean "no valid operation starts here"
5        lookup = [-1] * len(s)
6        
7        for i in range(len(indices)):
8            idx = indices[i]
9            src = sources[i]
10            
11            # CRITICAL: Only mark the operation as valid if the source matches
12            if s.startswith(src, idx):
13                lookup[idx] = i
14        
15        # 2. Build the result string by traversing the original
16        res = []
17        i = 0
18        while i < len(s):
19            if lookup[i] != -1:
20                # If a valid operation starts here, add the target
21                op_idx = lookup[i]
22                res.append(targets[op_idx])
23                # Jump the pointer forward by the length of the SOURCE string
24                i += len(sources[op_idx])
25            else:
26                # Otherwise, keep the original character
27                res.append(s[i])
28                i += 1
29                
30        return "".join(res)