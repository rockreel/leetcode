import unittest

from l0119_pascals_triangle_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 3, 3, 1], Solution().getRow(3))