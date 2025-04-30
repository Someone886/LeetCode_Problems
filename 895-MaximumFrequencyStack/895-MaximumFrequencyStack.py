# Last updated: 4/29/2025, 9:40:40 PM
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.occurence = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])

        self.occurence[self.freq[val]].append(val)

    def pop(self) -> int:
        max_occurence_list = self.occurence[self.max_freq]
        last_ele = max_occurence_list.pop()

        self.freq[last_ele] -= 1
        
        if not max_occurence_list:
            self.max_freq -= 1
        
        return last_ele


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()