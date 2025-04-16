# Last updated: 4/16/2025, 8:17:29 AM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbors = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbors[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        diff = 1

        while q:
            for i in range(len(q)):
                next_word = q.popleft()

                for j in range(len(next_word)):
                    pattern = next_word[:j] + "*" + next_word[j + 1:]

                    for neighbor in neighbors[pattern]:
                        if neighbor == endWord:
                            return diff + 1

                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            
            diff += 1

        return 0
        