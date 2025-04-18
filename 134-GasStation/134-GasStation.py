# Last updated: 4/18/2025, 6:54:25 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        gas_left = 0
        ans = 0

        # starting from ans, if there is no enough gas to reach i, #
        # then given that we have enough gas to reach every gas station, 
        # there must be another start point >= i + 1 to reach every gas station.
        for i in range(len(gas)):
            gas_left += (gas[i] - cost[i])

            if gas_left < 0:
                gas_left = 0
                ans = i + 1
        
        return ans
        