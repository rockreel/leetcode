class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        left_gas = [g - c for g, c in zip(gas, cost)]
        # The first postive left gas position after most deficit
        # position must be the starting point.
        idx = left_gas.index(min(left_gas))
        while left_gas[idx] < 0:
            idx += 1
            if idx > len(gas) - 1:
                idx = 0
        return idx

