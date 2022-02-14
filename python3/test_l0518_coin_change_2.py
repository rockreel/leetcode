import unittest

from l0518_coin_change_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().change(5, [1, 2, 5]))
        self.assertEqual(0, Solution().change(3, [2]))
        self.assertEqual(1, Solution().change(10, [10]))

