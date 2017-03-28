# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted([(i.start, i.end) for i in intervals])
        merged_intervals =[]
        for i in intervals:
            if not merged_intervals or merged_intervals[-1][1] < i[0]:
                merged_intervals.append(i)
            else:
                merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], i[1]))
        return [Interval(i[0], i[1]) for i in merged_intervals]

