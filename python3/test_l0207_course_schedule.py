import unittest

from l0207_course_schedule import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().canFinish(2, [[1, 0]]))
        self.assertEqual(False, Solution().canFinish(2, [[1, 0], [0, 1]]))
