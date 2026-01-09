# Last updated: 1/9/2026, 4:15:07 PM
1class Solution:
2    def compress(self, chars: list[str]) -> int:
3        n = len(chars)
4        write = 0  # Where we write the result
5        read = 0   # Where we are currently reading
6        
7        while read < n:
8            char = chars[read]
9            count = 0
10            
11            # Count the occurrences of the current character
12            while read < n and chars[read] == char:
13                read += 1
14                count += 1
15            
16            # Write the character
17            chars[write] = char
18            write += 1
19            
20            # If count > 1, write the digits of the count
21            if count > 1:
22                for digit in str(count):
23                    chars[write] = digit
24                    write += 1
25                    
26        return write