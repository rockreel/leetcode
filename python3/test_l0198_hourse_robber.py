import unittest

from l0198_house_robber import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))
        self.assertEqual(12, Solution().rob([2, 7, 9, 3, 1]))
