import unittest

from l0306_additive_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isAdditiveNumber('112358'))
        self.assertEqual(True, Solution().isAdditiveNumber('199100199'))
