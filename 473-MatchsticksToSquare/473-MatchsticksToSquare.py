# Last updated: 6/22/2025, 2:51:18 PM
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        match_sum = sum(matchsticks)
        if match_sum % 4 != 0:
            return False
        
        side_length = match_sum // 4
        matchsticks.sort(reverse = True)

        sides = [0] * 4

        def backtrack(index):
            if index == len(matchsticks):
                return True
            
            # for each of the 4 sides
            for j in range(4):
                if sides[j] + matchsticks[index] <= side_length:
                    # put the match at this side
                    sides[j] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[j] -= matchsticks[index]

                    """
                    Explanation:
                    If sides[j] = 0, it means this is the first time we've added values to that side.
                    If the backtrack search fails when adding the values to sides[j] and it remains 0, 
                    it will also fail for all sides from sides[j+1:].
                    Because we are simply going through the previous recursive tree again for a different j+1 position.
                    So we can effectively break from the for loop or directly return False.
                    """
                    if sides[j] == 0:
                        break
            
            return False
        
        return backtrack(0)
