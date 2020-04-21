from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(s1: str, s2: str) -> int:
            if s1 + s2 > s2 + s1:
                return -1
            else:
                return 1
            
        number = ''.join(sorted([str(n) for n in nums], key=cmp_to_key(compare)))

        return number if number[0] != '0' else '0'
