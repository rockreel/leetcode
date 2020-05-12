from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0, 1]
        while len(result) < num + 1:
            result.extend([x+1 for x in result])
        return result[:num+1]
