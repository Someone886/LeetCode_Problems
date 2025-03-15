class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        len_word = len(word)
        
        def helper(r, c, char, len_string):
            
            if len_string == len_word:
                return 1
            
            if len_string > len_word:
                return 0
            
            if r < 0 or r > m - 1 or c < 0 or c > n - 1:
                return 0
            
            letter = board[r][c]
            
            if letter != word[len_string]:
                return 0
            
            else:
                board[r][c] = ''
                
                found = helper(r-1, c, letter, len_string + 1)
                if found:
                    return 1
                
                found = helper(r+1, c, letter, len_string + 1)
                if found:
                    return 1
                
                found = helper(r, c-1, letter, len_string + 1)
                if found:
                    return 1
                
                found = helper(r, c+1, letter, len_string + 1)
                if found:
                    return 1
                
                board[r][c] = letter
                
            return 0
        
        cnt = Counter(c for row in board for c in row)
        # This line checks if the board has at least as many occurrences of each character as needed to form the given word.
        if not cnt >= Counter(word):
            return False

        # This conditional checks which end of the word is less common on the board and potentially reverses the word.
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        for r in range(m):
            for c in range(n):
                found = helper(r, c, '', 0)
                if found:
                    return True
                
        return False