import unittest

from l0246_strobogrammatic_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isStrobogrammatic('69'))
        self.assertEqual(False, Solution().isStrobogrammatic('68'))
