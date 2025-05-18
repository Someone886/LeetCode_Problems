# Last updated: 5/18/2025, 1:52:02 AM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1  # Outgoing trust (trusts someone)
            trust_score[b] += 1  # Incoming trust (is trusted)

        # Identify the judge
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1


'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = defaultdict(list)
        trusted = [0] * n

        for t in trust:
            truster, trustee = t[0], t[1]
            trusted[trustee - 1] += 1

            trusting[truster].append(trustee)
        
        for i in range(len(trusted)):
            trusted_cnt = trusted[i]
            if trusted_cnt == n - 1:
                if len(trusting[i + 1]) == 0:
                    return i + 1
        
        return -1
'''