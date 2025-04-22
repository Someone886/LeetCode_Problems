class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            min_len = min(len(word_1), len(word_2))

            if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
                return ""

            for j in range(min_len):
                if word_1[j] != word_2[j]:
                    adj[word_1[j]].add(word_2[j])
                    break

        # if visit a visiting = True node, then cycle, return invalid
        # if visit a visiting = False -> visited node, then not a cycle, just skip
        visiting = {}
        res = []

        # post-order traversal
        def dfs(char):
            if char in visiting:
                return visiting[char]               # true = cycle, false = skip
            
            visiting[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True                     # true = cycle, false = skip
            
            visiting[char] = False
            res.append(char)

            return False