# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        max_num_points = 0
        from collections import defaultdict
        for p0 in points:
            angle_map = defaultdict(int)
            num_same_as_p0 = 0
            for p1 in points:
                if p1.x == p0.x and p1.y == p0.y:
                    num_same_as_p0 += 1
                else:
                    if p0.x == p1.x:  # On a vertical line.
                        angle_map[float('inf')] += 1
                    else:
                        angle = float(p1.y - p0.y) / float(p1.x - p0.x)
                        angle_map[angle] += 1
            if angle_map:
                max_points_with_p0 = max([v for _, v in angle_map.iteritems()]) + num_same_as_p0
            else:
                max_points_with_p0 = num_same_as_p0
            max_num_points = max(max_num_points, max_points_with_p0)

        return max_num_points

