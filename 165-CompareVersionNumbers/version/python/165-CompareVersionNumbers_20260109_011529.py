# Last updated: 1/9/2026, 1:15:29 AM
1class Solution:
2    def compareVersion(self, version1: str, version2: str) -> int:
3        # Split into lists of strings
4        v1 = version1.split(".")
5        v2 = version2.split(".")
6        
7        # Iterate through the longest list
8        for i in range(max(len(v1), len(v2))):
9            # Get the integer value or 0 if index is out of bounds
10            # This handles cases like "1.1" vs "1.1.0.1" seamlessly
11            n1 = int(v1[i]) if i < len(v1) else 0
12            n2 = int(v2[i]) if i < len(v2) else 0
13            
14            if n1 > n2:
15                return 1
16            elif n1 < n2:
17                return -1
18        
19        # If all segments compared are equal
20        return 0