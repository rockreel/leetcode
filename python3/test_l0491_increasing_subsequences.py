import unittest

from l0491_increasing_subsequences import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]], 
            Solution().findSubsequences([4,6,7,7]))
        self.assertEqual(
            [[4,4]], 
            Solution().findSubsequences([4,4,3,2,1]))
