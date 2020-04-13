import unittest

from l0097_interleaving_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
        self.assertEqual(False, Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))