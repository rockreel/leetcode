from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = [0] * 11
        for b in bills:
            if b == 5:
                bill_count[5] += 1
            elif b == 10:
                bill_count[5] -= 1
                bill_count[10] += 1
            else:
                if bill_count[10] > 0:
                    bill_count[10] -= 1
                    bill_count[5] -= 1
                else:
                    bill_count[5] -= 3
            if bill_count[5] < 0:
                return False
        return True