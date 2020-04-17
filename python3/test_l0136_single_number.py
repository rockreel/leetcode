import unittest

from l0136_single_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().singleNumber([2, 2, 1]))
        self.assertEqual(4, Solution().singleNumber([4, 1, 2, 1, 2]))
