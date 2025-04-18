# Last updated: 4/18/2025, 7:29:39 PM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groups = [[] for i in range(len(hand) // groupSize)]

        for num in hand:
            classified = False

            for group in groups:
                if len(group) == groupSize:
                    continue
                
                if len(group) == 0:
                    group.append(num)
                    classified = True
                    break
                
                elif num == group[-1] + 1:
                    group.append(num)
                    classified = True
                    break
            
            if not classified:
                return False
            
        return True