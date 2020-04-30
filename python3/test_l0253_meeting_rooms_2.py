import unittest

from l0253_meeting_rooms_2 import Solution
from l0253_meeting_rooms_2 import Interval

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(1, Solution().minMeetingRooms([Interval(2, 7)]))
