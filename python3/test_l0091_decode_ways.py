import unittest

from l0091_decode_ways import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().numDecodings('12'))
        self.assertEqual(3, Solution().numDecodings('226'))
        self.assertEqual(0, Solution().numDecodings('06'))