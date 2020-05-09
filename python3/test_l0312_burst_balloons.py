import unittest

from l0312_burst_balloons import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(167, Solution().maxCoins([3, 1, 5, 8]))
