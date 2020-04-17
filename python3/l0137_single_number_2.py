from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n_count = Counter(nums)
        return [n for n, c in n_count.items() if c == 1][0]
