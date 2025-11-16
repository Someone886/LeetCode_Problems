# Last updated: 11/16/2025, 8:08:51 AM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        word_in_board = set()
        path = ''
        seen = set()
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, curr_node):
            nonlocal path, seen, word_in_board
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            
            if (r, c) in seen:
                return

            if board[r][c] not in curr_node.children:
                return
            
            path += board[r][c]
            seen.add((r, c))
            curr_node = curr_node.children[board[r][c]]
            if curr_node.end:
                word_in_board.add(path)

            for dr, dc in direction:    
                dfs(r + dr, c + dc, curr_node)

            seen.remove((r, c))
            path = path[:-1]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root)
        
        return list(word_in_board)
            
