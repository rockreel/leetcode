from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_sum = [0] * len(triangle)
        for row in triangle:
            new_sum = [0] * len(triangle)
            for i, n in enumerate(row):
                if i == 0:
                    new_sum[i] = n + min_sum[0]
                elif i == len(row) - 1:
                    new_sum[i] = n + min_sum[i-1]
                else:
                    new_sum[i] = n + min(min_sum[i-1], min_sum[i])
            min_sum = list(new_sum)
        return min(min_sum)