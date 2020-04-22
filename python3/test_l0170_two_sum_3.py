import unittest

from l0170_two_sum_3 import TwoSum

class Test(unittest.TestCase):
    
    def test_solution(self):
        two_sum = TwoSum()
        two_sum.add(1)
        two_sum.add(3)
        two_sum.add(5)
        self.assertEqual(True, two_sum.find(4))
        self.assertEqual(False, two_sum.find(7))
