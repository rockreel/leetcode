import unittest

from l0740_delete_and_earn import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().deleteAndEarn([3, 4, 2]))
        self.assertEqual(9, Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
