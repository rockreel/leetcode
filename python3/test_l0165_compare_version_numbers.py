import unittest

from l0165_compare_version_numbers import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(-1, Solution().compareVersion('1.0', '1.1'))
        self.assertEqual(1, Solution().compareVersion('1.0.1', '1'))
        self.assertEqual(-1, Solution().compareVersion('7.5.2.4', '7.5.3'))
        self.assertEqual(0, Solution().compareVersion('1.01', '1.001'))
        self.assertEqual(0, Solution().compareVersion('1.0', '1.0.0'))