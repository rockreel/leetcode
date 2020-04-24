import unittest

from l0210_course_schedule_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertTrue(
            Solution().findOrder(2, [[1, 0]]) in [[0, 1]])
        self.assertTrue(
            Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in
            [[0, 1, 2, 3], [0, 2, 1, 3]])
        self.assertTrue(
            Solution().findOrder(3, [[1, 0], [1, 2], [0, 1]]) in [[]])