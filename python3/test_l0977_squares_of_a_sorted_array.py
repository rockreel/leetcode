import unittest

from l0977_squares_of_a_sorted_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [0, 1, 9, 16, 100], 
            Solution().sortedSquares([-4, -1, 0, 3, 10]))
        self.assertEqual(
            [4, 9, 9, 49, 121], 
            Solution().sortedSquares([-7, -3, 2, 3, 11]))
