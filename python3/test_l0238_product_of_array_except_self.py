import unittest

from l0238_product_of_array_except_self import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf([1, 2, 3, 4]))