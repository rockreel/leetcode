from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            curr_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if curr_sum < 0:
                start = i + 1
                curr_sum = 0
        if total_sum < 0:
            return -1
        else:
            return start