from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points)
        count = 1
        pos = points[0][1]
        for i in range(len(points)):
            if points[i][0] <= pos:
                if points[i][1] < pos:
                    pos = points[i][1]
                else:
                    continue
            else:
                pos = points[i][1]
                count += 1
        return count
