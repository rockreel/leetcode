import unittest

from l0259_3sum_smaller import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().threeSumSmaller([-2, 0, 1, 3], 2))
        self.assertEqual(3, Solution().threeSumSmaller([-2, 0, -1, 3], 2))
