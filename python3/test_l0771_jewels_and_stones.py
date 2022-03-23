import unittest

from l0771_jewels_and_stones import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(0, Solution().numJewelsInStones("z", "ZZ"))

        