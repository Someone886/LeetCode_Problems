class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        max_length = 0
        length = 0
        left, right = 0, 1
        n = len(s)
        hash_map = {}
        
        while left < n and right <= n:
            c = s[right - 1]
            if c in hash_map and hash_map[c] >= left:
                left = hash_map[c] + 1

            hash_map[c] = right - 1
            if right - left > max_length:
                max_length = right - left

            right += 1

        return max_length