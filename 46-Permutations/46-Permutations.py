# Last updated: 12/27/2025, 2:13:17 AM
1class Solution(object):
2    def permute(self, nums):
3        ans = []
4        comb = []
5        picked = [False] * len(nums)
6
7        def helper():
8            if len(comb) == len(nums):
9                ans.append(comb.copy())
10            
11            for i in range(len(nums)):
12                if picked[i]:
13                    continue
14                comb.append(nums[i])
15                picked[i] = True
16                helper()
17                comb.pop()
18                picked[i] = False
19        
20        helper()
21        return ans
22
23# class Solution:
24#     def permute(self, nums: List[int]) -> List[List[int]]:
25#         index_set = set([i for i in range(len(nums))])
26#         ans = []
27#         curr = []
28
29#         def helper(index_set_left):
30#             if len(curr) == len(nums):
31#                 ans.append(curr.copy())
32#                 return
33            
34#             for i in index_set_left:
35#                 curr.append(nums[i])
36#                 new_index_set_left = index_set_left.copy()
37#                 new_index_set_left.remove(i)
38#                 helper(new_index_set_left)
39
40#                 curr.pop()
41        
42#         helper(index_set)
43#         return ans