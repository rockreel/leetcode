import unittest

from l0263_ugly_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isUgly(6))
        self.assertEqual(True, Solution().isUgly(8))
        self.assertEqual(False, Solution().isUgly(14))