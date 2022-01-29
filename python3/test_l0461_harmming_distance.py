import unittest

from l0461_harmming_distance import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().hammingDistance(1, 4))
        self.assertEqual(1, Solution().hammingDistance(3, 1))