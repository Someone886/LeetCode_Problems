# Last updated: 1/6/2026, 9:06:33 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4        
5        # We use left < right because we are narrowing down to a single element
6        while left < right:
7            mid = left + (right - left) // 2
8            
9            # If mid element is greater than the rightmost element,
10            # the minimum must be in the right part (mid + 1 to right)
11            if nums[mid] > nums[right]:
12                left = mid + 1
13            # Otherwise, the minimum is either mid or to the left of mid
14            else:
15                right = mid
16        
17        # After the loop, left == right, pointing to the minimum element
18        return nums[left]