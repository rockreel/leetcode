import unittest

from l0223_rectangle_area import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(45, Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

