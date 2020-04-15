import unittest

from l0115_distinct_subsequences import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().numDistinct('rabbbit', 'rabbit'))
        self.assertEqual(5, Solution().numDistinct('babgbag', 'bag'))