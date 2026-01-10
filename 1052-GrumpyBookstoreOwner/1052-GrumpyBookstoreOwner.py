# Last updated: 1/10/2026, 3:39:21 PM
1class Solution:
2    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
3        if len(customers) <= minutes:
4            return sum(customers)
5        
6        n = len(customers)
7        left = 0
8        right = minutes
9        satisfied_in_window = sum(customers[left:right])
10        for i in range(right, n):
11            if grumpy[i] == 0:
12                satisfied_in_window += customers[i]
13        max_satisfied = satisfied_in_window
14
15        while right < n:
16            if grumpy[right] == 1:
17                satisfied_in_window += customers[right]
18            
19            if grumpy[left] == 1:
20                satisfied_in_window -= customers[left]
21            
22            max_satisfied = max(max_satisfied, satisfied_in_window)
23
24            right += 1
25            left += 1
26        
27        return max_satisfied