# Last updated: 4/9/2025, 2:02:39 PM
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        n = len(board)
        m = len(board[0])

        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[None] = None
        
        word_set = set()

        def dfs(r, c, seen, node, word_set):

            if None in node:
                word_set.add(seen)

            if r < 0 or r > n - 1 or c < 0 or c > m - 1:
                return
            
            char = board[r][c]
            if char == -1:
                return
            
            board[r][c] = -1

            if char in node:
                dfs(r + 1, c, seen + char, node[char], word_set)
                dfs(r - 1, c, seen + char, node[char], word_set)
                dfs(r, c + 1, seen + char, node[char], word_set)
                dfs(r, c - 1, seen + char, node[char], word_set)
                   
            
            board[r][c] = char
        
        for r in range(n):
            for c in range(m):
                dfs(r, c, '', trie, word_set)
        
        return list(word_set)