class Solution:
    # count - occurence of symbol with maximum number of occurences
    # (n + 1) - number of elements in repeated interval 'A _ _' or 'A B _'.
    # (count - 1) - maximum occurences of character with maximum maximum occurence except the last occurence of that character
    # (count - 1) * (n + 1) - minimum number of symbols except the last one
    # k - number of characters with maximum occurence.

    # (count - 1) * (n + 1) + k

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        sorted_counts = sorted(counts.values(), reverse=True)

        case_1 = len(tasks)
        case_2 = (sorted_counts[0] - 1) * (n + 1) + sorted_counts.count(sorted_counts[0])

        return max(case_1, case_2)