import unittest

from l0213_house_robber_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().rob([2, 3, 2]))
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))
