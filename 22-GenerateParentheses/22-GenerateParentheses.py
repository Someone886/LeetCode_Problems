class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        brackets = ['(', ')']
        
        if n == 0:
            return ans
        
        def helper(n_left, n_right, string):
            if n_left == 0 and n_right == 0:
                ans.append(string)
                return
            
            if n_left == 0:
                for i in range(n_right):
                    string += ')'
                ans.append(string)
                return
            
            if n_left < n_right:
                string = string + '('
                helper(n_left - 1, n_right, string)
                string = string[:-1]
                
                string = string + ')'
                helper(n_left, n_right - 1, string)
                string = string[:-1]
            
            elif n_left == n_right:
                string = string + '('
                helper(n_left - 1, n_right, string)
                string = string[:-1]
            
            else:
                string = string + ')'
                helper(n_left, n_right-1, string)
                string = string[:-1]
                
            return
    
        helper(n, n, '')
        
        return ans
        