import unittest

from l0152_maximum_product_subarray import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, Solution().maxProduct([-2, 0, -1]))

