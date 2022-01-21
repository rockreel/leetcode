import unittest

from l0387_first_unique_character_in_a_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(0, Solution().firstUniqChar('leetcode'))
        self.assertEqual(2, Solution().firstUniqChar('loveleetcode'))
        self.assertEqual(-1, Solution().firstUniqChar('aabb'))
