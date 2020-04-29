import unittest

from l0260_single_number_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([3, 5], sorted(Solution().singleNumber([1, 2, 1, 3, 2, 5])))
