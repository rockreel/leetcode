import unittest

from l0044_wildcard_matching import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(False, Solution().isMatch('aa', 'a'))
        self.assertEqual(True, Solution().isMatch('aa', '*'))
        self.assertEqual(False, Solution().isMatch('cb', '?a'))
        self.assertEqual(True, Solution().isMatch('adceb', '*a*b'))
        self.assertEqual(False, Solution().isMatch('acdcb', 'a*c?b'))