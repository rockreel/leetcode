import unittest

from l0096_unique_binary_search_trees import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().numTrees(3))
        self.assertEqual(1767263190, Solution().numTrees(19))
