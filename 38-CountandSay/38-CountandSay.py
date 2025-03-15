class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)

        left = 0
        right = 0
        count = 0

        ans = ""
        n = len(prev)

        while left < n and right < n:
            c_left = prev[left]
            c_right = prev[right]

            if c_left == c_right:
                count += 1
                right += 1
            else:
                ans += str(count) + c_left
                left = right
                count = 1
                right += 1

        c_left = prev[left]
        ans += str(count) + c_left

        return ans
        