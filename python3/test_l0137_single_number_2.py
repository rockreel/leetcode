import unittest

from l0137_single_number_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().singleNumber([2, 2, 3, 2]))
        self.assertEqual(99, Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
