from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if i == 0 or j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(row_prev[j-1]+row_prev[j])
            row_prev = row
        return row