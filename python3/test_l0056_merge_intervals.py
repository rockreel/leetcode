import unittest

from l0056_merge_intervals import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            [[1, 6],[8, 10],[15, 18]],
            Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
        self.assertEqual(
            [[1, 5]],
            Solution().merge([[1, 4], [4, 5]]))

