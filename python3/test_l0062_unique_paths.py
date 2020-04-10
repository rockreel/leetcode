import unittest

from l0062_unique_paths import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().uniquePaths(3, 2))
        self.assertEqual(28, Solution().uniquePaths(7, 3))