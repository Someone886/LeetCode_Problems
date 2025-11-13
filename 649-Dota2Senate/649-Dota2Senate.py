# Last updated: 11/13/2025, 4:14:31 AM
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        diff = 0 # R - C
        i = 0

        while i < len(senate):
            c = senate[i]
            if c == 'R':
                if diff < 0: # more C than R before index i
                    senate.append('D') # in the next round, the D in the front will speak again
                diff += 1
            else:
                if diff > 0: # more R than C before index i
                    senate.append('R') # in the next round, the R in the front will speak again
                diff -= 1
            i += 1

        return "Radiant" if diff > 0 else "Dire"