from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        maximums = []
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
            if i - queue[0] == k:
                queue.popleft()
            if i >= k - 1:
                maximums.append(nums[queue[0]])
        return maximums