# Last updated: 1/5/2026, 10:09:53 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [1] * n
5        
6        # Step 1: Calculate Prefix Products
7        # After this, res[i] contains the product of all elements to the left of i
8        prefix = 1
9        for i in range(n):
10            res[i] = prefix
11            prefix *= nums[i]
12            
13        # Step 2: Calculate Suffix Products on the fly
14        # Multiply the existing prefix product by the suffix product
15        suffix = 1
16        for i in range(n - 1, -1, -1):
17            res[i] *= suffix
18            suffix *= nums[i]
19            
20        return res