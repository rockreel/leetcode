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