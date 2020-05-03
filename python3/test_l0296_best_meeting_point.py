import unittest

from l0296_best_meeting_point import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6,
            Solution().minTotalDistance([
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0]
            ]))
        self.assertEqual(
            14,
            Solution().minTotalDistance([
                [1, 1, 0, 0, 1],
                [1, 0, 1, 0, 0],
                [0, 0, 1, 0, 1]
            ]))