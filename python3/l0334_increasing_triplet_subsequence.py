from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s1, s2 = float('inf'), float('inf')
        for n in nums:
            if n > s2:
                return True
            if n > s1:
                s2 = n
            else:
                s1 = n
        return False
