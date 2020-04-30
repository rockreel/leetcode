"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            # End time will sort before start time, so back-to-back meetings can drop room num first.
            times.append((interval.end, -1))
        times = sorted(times)
        min_rooms = 0
        rooms = 0
        for t in times:
            if t[1] == 1:
                rooms += 1
            else:
                rooms -= 1
            min_rooms = max(min_rooms, rooms)
        return min_rooms

