import unittest

from l0118_pascals_triangle import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ],
            Solution().generate(5))