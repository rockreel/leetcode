from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        checked = set([])
        for n in arr:
            if n in checked:
                return True
            checked.add(2*n)
            if n % 2 == 0:
                checked.add(n // 2)
        return False