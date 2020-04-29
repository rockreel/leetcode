import unittest

from l0264_ugly_number_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(12, Solution().nthUglyNumber(10))
