from typing import List
import unittest

from l0049_group_anagrams import Solution

class Test(unittest.TestCase):

    def sort_solution(self, result: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(r) for r in result])

    def test_solution(self):
        self.assertEqual(
            self.sort_solution([['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]),
            self.sort_solution(Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])))