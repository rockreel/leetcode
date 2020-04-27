import bisect
from typing import List

class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for building in buildings:
            # Break each building into start and end points.
            # Sort left point before right point.
            # For left point, sort higher point before lower point.
            # This to avoid future dedup.
            points.append((building[0], -1, -building[2]))
            points.append((building[1], 1, building[2]))
        points = sorted(points)
        heights = [0]  # A sorted heights to keep track of maximum height.
        skylines = []
        for x, t, h in points:
            if t == -1:
                h = -h
                if h > heights[-1]:
                    skylines.append([x, h])
                bisect.insort_left(heights, h)
            else:
                heights.remove(h)
                if h > heights[-1]:
                    skylines.append([x, heights[-1]])
        return skylines
