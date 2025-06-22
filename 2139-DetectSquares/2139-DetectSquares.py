# Last updated: 6/22/2025, 2:50:36 PM
class DetectSquares:
    def __init__(self):
        self.trie = defaultdict(lambda : defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        x_map = self.trie[x]
        x_map[y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0

        x_map = self.trie[x]
        for y_value, y_count in x_map.items():
            y_dist = y_value - y
            if y_dist == 0:
                continue
            
            neg_y_dist = -y_dist

            cnt += self.trie[x][y_value] * \
                    self.trie[x + y_dist][y] * \
                    self.trie[x + y_dist][y_value]

            cnt += self.trie[x][y_value] * \
                    self.trie[x + neg_y_dist][y] * \
                    self.trie[x + neg_y_dist][y_value]

        return cnt
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)