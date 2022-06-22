import unittest

from l0376_wiggle_subsequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(6, Solution().wiggleMaxLength([1,7,4,9,2,5]))
        self.assertEqual(7, Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
        self.assertEqual(2, Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
