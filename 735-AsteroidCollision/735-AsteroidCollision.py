# Last updated: 1/10/2026, 8:04:06 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for asteroid in asteroids:
6            while stack and asteroid < 0 < stack[-1]: # ignore negative asteroids at the start of the stack
7                if stack[-1] < -asteroid:
8                    stack.pop()  # smaller one explodes, continue
9                elif stack[-1] == -asteroid:
10                    stack.pop()  # both explode
11                    break
12                else:
13                    break  # incoming one explodes
14            else:
15                stack.append(asteroid)
16
17        return stack
18
19# class Solution:    
20#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
21#         def sign(num):
22#             if num > 0:
23#                 return 1
24#             elif num < 0:
25#                 return -1
26#             else:
27#                 return 0
28        
29#         stack = []
30
31#         for asteroid in asteroids:
32#             if not stack:
33#                 stack.append(asteroid)
34#             else:
35#                 asteroid_left = asteroid
36#                 to_append = True
37
38#                 while stack and (sign(asteroid_left) < 0 and sign(stack[-1]) > 0):
39#                     top_asteroid = stack.pop()
40#                     if abs(top_asteroid) > abs(asteroid_left):
41#                         asteroid_left = top_asteroid
42#                         break
43#                     elif abs(top_asteroid) < abs(asteroid_left):
44#                         asteroid_left = asteroid_left
45#                     else:
46#                         to_append = False
47#                         break
48                
49#                 if to_append:
50#                     stack.append(asteroid_left)
51        
52#         return stack