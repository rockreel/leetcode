import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._shuffled = list(nums)

    def reset(self) -> List[int]:
        return self._nums

    def shuffle(self) -> List[int]:
        for i in range(len(self._shuffled)):
            idx = random.randrange(i, len(self._shuffled))
            self._shuffled[i], self._shuffled[idx] = self._shuffled[idx], self._shuffled[i]
        return self._shuffled

    def shuffleArrayPop(self) -> List[int]:
        result = []
        candidate = list(self._nums)
        while candidate:
            idx = random.randrange(len(candidate))
            result.append(candidate.pop(idx))
        return result
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()