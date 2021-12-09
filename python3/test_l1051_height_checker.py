import unittest

from l1051_height_checker import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3, 
            Solution().heightChecker([1, 1, 4, 2, 1, 3]))
        self.assertEqual(
            5, 
            Solution().heightChecker([5, 1, 2, 3, 4]))
        self.assertEqual(
            0, 
            Solution().heightChecker([1, 2, 3, 4, 5]))
