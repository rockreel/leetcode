from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numSquared = [n**2 for n in nums]
        i, j = 0, len(numSquared) - 1
        numSorted = []
        while i < j:
            if numSquared[i] > numSquared[j]:
                numSorted.append(numSquared[i])
                i += 1
            else:
                numSorted.append(numSquared[j])
                j -= 1
        numSorted.append(numSquared[i])
        return list(reversed(numSorted))
