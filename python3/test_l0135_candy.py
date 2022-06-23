import unittest

from l0135_candy import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().candy([1,0,2]))
        self.assertEqual(4, Solution().candy([1,2,2]))
