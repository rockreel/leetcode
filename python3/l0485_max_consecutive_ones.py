from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_one = False
        max_len = 0
        curr_len = 0
        for n in nums:
            if n == 1:
                if is_one:
                    curr_len += 1
                else:
                    curr_len = 1
                    is_one = True
                max_len = max(max_len, curr_len)
            elif is_one:
                is_one = False
        return max_len

    def findMaxConsecutiveOnesOld(self, nums: List[int]) -> int:
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