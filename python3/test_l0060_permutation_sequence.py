import unittest

from l0060_permutation_sequence import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('213', Solution().getPermutation(3, 3))
        self.assertEqual('2314', Solution().getPermutation(4, 9))