# Last updated: 5/17/2025, 1:02:58 AM
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = 0
        bill_10 = 0

        for bill in bills:
            if bill == 5:
                bill_5 += 1

            elif bill == 10:
                bill_5 -= 1
                bill_10 += 1

                if bill_5 < 0:
                    return False

            else:
                bill_5 -= 1
                
                if bill_10 == 0:
                    bill_5 -= 2
                else:
                    bill_10 -= 1
                
                if bill_5 < 0 or bill_10 < 0:
                    return False
        
        return True