# Last updated: 4/12/2025, 12:06:51 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []
        n = len(s)

        def check_palindrome(s):
            if s == s[::-1]:
                return True
            return False

        def helper(start, end):
            if end == n:
                if start == end:
                    ans.append(curr.copy())
                return
            
            partition = s[start : end + 1]
            if check_palindrome(partition):
                curr.append(partition)
                helper(end + 1, end + 1)
                curr.pop()
            
            helper(start, end + 1)
        
        helper(0, 0)
        return ans