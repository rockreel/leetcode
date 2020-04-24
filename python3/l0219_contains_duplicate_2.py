from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_count = defaultdict(int)
        for i, n in enumerate(nums):
            if i > k:
                num_count[nums[i-k-1]] -= 1
            num_count[n] += 1
            if num_count[n] > 1:
                return True
        return False