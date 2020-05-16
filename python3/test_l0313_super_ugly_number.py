import unittest

from l0313_super_ugly_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(32, Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
