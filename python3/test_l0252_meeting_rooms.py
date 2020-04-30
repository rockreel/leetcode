import unittest

from l0252_meeting_rooms import Solution
from l0252_meeting_rooms import Interval

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(False, Solution().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(True, Solution().canAttendMeetings([Interval(5, 8), Interval(9, 15)]))
