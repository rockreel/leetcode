from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        max_running_len = 0
        is_last_one = False
        for n in nums:
            if is_last_one:
                if n == 1:
                    max_running_len += 1
                else:
                    max_len = max(max_len, max_running_len)
                    max_running_len = 0
                    is_last_one = False
            elif n == 1:
                max_running_len = 1
                is_last_one = True
        max_len = max(max_len, max_running_len)
        return max_len