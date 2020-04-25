from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = None, None
        count1, count2 = 0, 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1 = n
                count1 = 1
            elif count2 == 0:
                c2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(c1)
        if count2 > len(nums) // 3:
            result.append(c2) 
        return result