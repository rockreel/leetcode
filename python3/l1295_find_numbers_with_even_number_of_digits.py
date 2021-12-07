from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def numOfDigit(num: int) -> int:
            if num == 0:
                return 1
            i = 0
            while num > 0:
                num = num // 10
                i += 1
            return i
        
        count = 0
        for n in nums:
            if numOfDigit(n) % 2 == 0:
                count += 1
                
        return count
