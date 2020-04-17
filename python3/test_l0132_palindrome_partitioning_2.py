import unittest

from l0132_palindrome_partitioning_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().minCut('aab'))
        self.assertEqual(2, Solution().minCut('leet'))