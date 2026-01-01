# Last updated: 1/1/2026, 4:22:51 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        current_num = 0
5        current_str = ""
6        
7        for char in s:
8            if char.isdigit():
9                # Build the number (handles multi-digits like 10, 100)
10                current_num = current_num * 10 + int(char)
11            elif char == "[":
12                # Save the current state to the stack
13                # We store the string built so far and the multiplier
14                stack.append((current_str, current_num))
15                # Reset for the new context inside the brackets
16                current_str = ""
17                current_num = 0
18            elif char == "]":
19                # Finish the current context
20                last_str, num = stack.pop()
21                # Multiply the current context and prepend the previous string
22                current_str = last_str + (num * current_str)
23            else:
24                # Regular character: just add to current working string
25                current_str += char
26                
27        return current_str
28
29'''
30class Solution:
31    def decodeString(self, s: str) -> str:
32        stack = []
33        
34        for char in s:
35            if char != "]":
36                # Push everything that isn't a closing bracket
37                stack.append(char)
38            else:
39                # 1. Extract the substring inside the brackets
40                string_to_multiply = ""
41                while stack and stack[-1] != "[":
42                    component = stack.pop()
43                    # Prepending is O(K) where K is string length
44                    string_to_multiply = component + string_to_multiply
45                
46                # 2. Pop the opening bracket '['
47                stack.pop()
48
49                # 3. BUG: This only pops ONE character. 
50                # If the number is "10", it only gets "0".
51                # Also fails if the number was previously joined as a string.
52                num_str = ""
53                while stack and stack[-1].isdigit():
54                    num_str = stack.pop() + num_str
55                
56                num = int(num_str)
57
58                # 4. Repeat and push back to stack
59                string_to_append = num * string_to_multiply
60                stack.append(string_to_append)
61        
62        # Join the remaining components in the stack
63        return "".join(stack)
64'''