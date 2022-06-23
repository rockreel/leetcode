import unittest

from l0860_lemonade_change import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().lemonadeChange([5,5,5,10,20]))
        self.assertEqual(False, Solution().lemonadeChange([5,5,10,10,20]))


