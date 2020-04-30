import unittest

from l0299_bulls_and_cows import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('1A3B', Solution().getHint('1807', '7810'))
        self.assertEqual('1A1B', Solution().getHint('1123', '0111'))
        self.assertEqual('3A0B', Solution().getHint('1122', '1222'))