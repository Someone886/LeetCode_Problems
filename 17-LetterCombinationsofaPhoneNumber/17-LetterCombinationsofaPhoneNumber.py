class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hash_map = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                    }
        
        ans = []

        if len(digits) == 0:
            return ans

        n = len(digits)

        def dfs(cur_index, string):
            if cur_index == n:
                ans.append(string)
                return
            
            possible_digits = hash_map[digits[cur_index]]
            for d in possible_digits:
                dfs(cur_index + 1, string + d)
            
            return
        
        dfs(0, '')

        return ans
        