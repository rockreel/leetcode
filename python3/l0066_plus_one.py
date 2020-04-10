from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list(digits)
        c = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] < 9:
                result[i] = result[i] + 1
                c = 0
                break
            else:
                result[i] = 0
                c = 1
        if c == 1:
            result.insert(0, 1)
        return result
