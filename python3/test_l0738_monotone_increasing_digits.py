import unittest

from l0738_monotone_increasing_digits import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(9, Solution().monotoneIncreasingDigits(10))
        self.assertEqual(1234, Solution().monotoneIncreasingDigits(1234))
        self.assertEqual(299, Solution().monotoneIncreasingDigits(332))

