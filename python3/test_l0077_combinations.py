import unittest

from l0077_combinations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]),
            sorted(Solution().combine(4, 2)))